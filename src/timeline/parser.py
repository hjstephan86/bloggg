#!/usr/bin/env python3
"""
Google Timeline Edits Parser - Complete Version with Distance Calculations
Properly parses Google Timeline edits with accurate GPS coordinate conversion and distance tracking
"""

import argparse
import json
import math
import os
from collections import defaultdict
from datetime import datetime, timedelta


class TimelineEditsParser:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.timeline_edits = []

    def load_timeline_edits(self, file_path=None):
        """Load ALL timeline edits from JSON file(s)"""
        if file_path:
            self.file_path = file_path

        if not self.file_path:
            raise ValueError("No file path provided")

        total_edits = 0

        # Check if it's a single file or directory
        if os.path.isfile(self.file_path):
            # Single file
            total_edits += self._load_single_file(self.file_path)
        elif os.path.isdir(self.file_path):
            # Directory - find all JSON files
            json_files = []
            for root, dirs, files in os.walk(self.file_path):
                for file in files:
                    if file.endswith(".json") and (
                        "timeline" in file.lower() or "edits" in file.lower()
                    ):
                        json_files.append(os.path.join(root, file))

            print(f"Found {len(json_files)} timeline JSON files")
            for file_path in json_files:
                edits_count = self._load_single_file(file_path)
                total_edits += edits_count
                print(f"  {os.path.basename(file_path)}: {edits_count} edits")
        else:
            print(f"Error: {self.file_path} is not a valid file or directory!")
            return False

        print(f"Total loaded: {total_edits} timeline edits")
        return True

    def _load_single_file(self, file_path):
        """Load timeline edits from a single JSON file"""
        edits_count = 0
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                if "timelineEdits" in data:
                    self.timeline_edits.extend(data["timelineEdits"])
                    edits_count = len(data["timelineEdits"])
                elif "timelineObjects" in data:
                    # Handle old format as well
                    for obj in data["timelineObjects"]:
                        converted_edit = self._convert_timeline_object(obj)
                        if converted_edit:
                            self.timeline_edits.append(converted_edit)
                            edits_count += 1

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return edits_count

    def _convert_timeline_object(self, timeline_obj):
        """Convert old timeline object format to timeline edit format"""
        if "activitySegment" in timeline_obj:
            segment = timeline_obj["activitySegment"]
            start_location = segment.get("startLocation", {})

            if "timestamp" in start_location:
                return {
                    "deviceId": "converted",
                    "rawSignal": {
                        "signal": {
                            "activityRecord": {
                                "detectedActivities": [
                                    {
                                        "activityType": segment.get(
                                            "activityType", "UNKNOWN"
                                        ),
                                        "probability": 0.8,
                                    }
                                ],
                                "timestamp": start_location["timestamp"],
                            }
                        }
                    },
                }
        return None

    def _convert_e7_to_decimal(self, e7_value):
        """Convert E7 format (degrees * 10^7) to decimal degrees with validation"""
        if e7_value is None:
            return None

        try:
            decimal_degrees = e7_value / 10000000.0
            # Basic validation - coordinates should be reasonable
            if abs(decimal_degrees) > 180:
                print(
                    f"Warning: Suspicious coordinate value {decimal_degrees} from E7 {e7_value}"
                )
            return decimal_degrees
        except (TypeError, ValueError) as e:
            print(f"Error converting E7 value {e7_value}: {e}")
            return None

    def parse_all_signals(self):
        """Parse all types of signals from timeline edits - fixed coordinate conversion"""
        activities = []
        positions = []
        wifi_scans = []

        print("Parsing timeline edits...")

        for i, edit in enumerate(self.timeline_edits):
            device_id = edit.get("deviceId", "unknown")
            raw_signal = edit.get("rawSignal", {})
            signal = raw_signal.get("signal", {})
            additional_timestamp = raw_signal.get("additionalTimestamp")

            # Parse activity records
            if "activityRecord" in signal:
                activity_record = signal["activityRecord"]
                timestamp_str = activity_record.get("timestamp")
                detected_activities = activity_record.get("detectedActivities", [])

                if timestamp_str:
                    try:
                        timestamp = datetime.fromisoformat(
                            timestamp_str.replace("Z", "+00:00")
                        )

                        # Get primary activity (highest probability)
                        primary_activity = None
                        if detected_activities:
                            primary_activity = max(
                                detected_activities,
                                key=lambda x: x.get("probability", 0),
                            )

                        activity_data = {
                            "edit_index": i,
                            "timestamp": timestamp,
                            "device_id": device_id,
                            "signal_type": "activity",
                            "primary_activity": primary_activity.get("activityType")
                            if primary_activity
                            else "UNKNOWN",
                            "primary_probability": primary_activity.get(
                                "probability", 0
                            )
                            if primary_activity
                            else 0,
                            "all_activities": detected_activities,
                            "additional_timestamp": additional_timestamp,
                            "latitude": None,
                            "longitude": None,
                            "accuracy_m": None,
                        }
                        activities.append(activity_data)

                    except Exception as e:
                        print(f"Error parsing activity timestamp {timestamp_str}: {e}")

            # Parse position data with improved coordinate handling
            elif "position" in signal:
                position = signal["position"]
                timestamp_str = position.get("timestamp")
                point = position.get("point", {})

                if timestamp_str and point:
                    try:
                        timestamp = datetime.fromisoformat(
                            timestamp_str.replace("Z", "+00:00")
                        )

                        # Convert from E7 format with proper validation
                        lat_e7 = point.get("latE7")
                        lng_e7 = point.get("lngE7")

                        lat = self._convert_e7_to_decimal(lat_e7)
                        lng = self._convert_e7_to_decimal(lng_e7)

                        if lat is None or lng is None:
                            print(
                                f"Skipping position with invalid coordinates: lat_e7={lat_e7}, lng_e7={lng_e7}"
                            )
                            continue

                        # Convert accuracy from mm to meters with validation
                        accuracy_mm = position.get("accuracyMm", 0)
                        accuracy_m = accuracy_mm / 1000.0 if accuracy_mm else 0

                        position_data = {
                            "edit_index": i,
                            "timestamp": timestamp,
                            "device_id": device_id,
                            "signal_type": "position",
                            "latitude": lat,
                            "longitude": lng,
                            "lat_e7": lat_e7,  # Keep original for debugging
                            "lng_e7": lng_e7,  # Keep original for debugging
                            "accuracy_m": accuracy_m,
                            "source": position.get("source", "UNKNOWN"),
                            "altitude": position.get("altitudeMeters"),
                            "speed": position.get("speedMetersPerSecond"),
                            "additional_timestamp": additional_timestamp,
                            "primary_activity": None,
                            "primary_probability": None,
                        }
                        positions.append(position_data)

                    except Exception as e:
                        print(f"Error parsing position timestamp {timestamp_str}: {e}")

            # Parse WiFi scans
            elif "wifiScan" in signal:
                wifi_scan = signal["wifiScan"]
                delivery_time_str = wifi_scan.get("deliveryTime")
                devices = wifi_scan.get("devices", [])

                if delivery_time_str:
                    try:
                        timestamp = datetime.fromisoformat(
                            delivery_time_str.replace("Z", "+00:00")
                        )

                        wifi_data = {
                            "edit_index": i,
                            "timestamp": timestamp,
                            "device_id": device_id,
                            "signal_type": "wifi",
                            "wifi_devices": len(devices),
                            "strongest_signal": max(
                                [d.get("rawRssi", -100) for d in devices]
                            )
                            if devices
                            else None,
                            "additional_timestamp": additional_timestamp,
                            "latitude": None,
                            "longitude": None,
                            "primary_activity": None,
                        }
                        wifi_scans.append(wifi_data)

                    except Exception as e:
                        print(f"Error parsing wifi timestamp {delivery_time_str}: {e}")

        print(
            f"Parsed {len(activities)} activity records, {len(positions)} positions, {len(wifi_scans)} wifi scans"
        )

        # Debug coordinate validation
        if positions:
            self._validate_coordinates(positions)

        return activities, positions, wifi_scans

    def _validate_coordinates(self, positions):
        """Validate and report on coordinate quality"""
        print(f"\n=== COORDINATE VALIDATION ===")

        valid_coords = [p for p in positions if p["latitude"] and p["longitude"]]
        if not valid_coords:
            print("No valid coordinates found!")
            return

        # Calculate coordinate bounds
        lats = [p["latitude"] for p in valid_coords]
        lngs = [p["longitude"] for p in valid_coords]

        min_lat, max_lat = min(lats), max(lats)
        min_lng, max_lng = min(lngs), max(lngs)

        print(f"Coordinate bounds:")
        print(
            f"  Latitude: {min_lat:.7f} to {max_lat:.7f} (span: {max_lat - min_lat:.7f}°)"
        )
        print(
            f"  Longitude: {min_lng:.7f} to {max_lng:.7f} (span: {max_lng - min_lng:.7f}°)"
        )

        # Calculate maximum distance
        max_distance = 0
        for i in range(len(valid_coords)):
            for j in range(i + 1, len(valid_coords)):
                distance = self.haversine_distance(
                    valid_coords[i]["latitude"],
                    valid_coords[i]["longitude"],
                    valid_coords[j]["latitude"],
                    valid_coords[j]["longitude"],
                )
                max_distance = max(max_distance, distance)

        print(f"  Maximum distance between any two points: {max_distance:.1f} meters")

        # Show sample coordinates for verification
        print(f"\nSample coordinates (first 5 positions):")
        for i, pos in enumerate(valid_coords[:5]):
            print(
                f"  {i + 1}. {pos['timestamp'].strftime('%H:%M:%S')}: "
                f"({pos['latitude']:.7f}, {pos['longitude']:.7f}) "
                f"from E7({pos['lat_e7']}, {pos['lng_e7']})"
            )

    def correlate_activities_with_positions(self, activities, positions):
        """Correlate activity records with nearby position data"""
        print("Correlating activities with GPS positions...")

        # Sort both by timestamp
        activities.sort(key=lambda x: x["timestamp"])
        positions.sort(key=lambda x: x["timestamp"])

        enhanced_records = []

        for activity in activities:
            activity_time = activity["timestamp"]

            # Find closest position within 5 minutes
            closest_position = None
            min_time_diff = timedelta(minutes=5)

            for position in positions:
                time_diff = abs(position["timestamp"] - activity_time)
                if time_diff < min_time_diff:
                    min_time_diff = time_diff
                    closest_position = position

            # Create enhanced record
            enhanced_record = activity.copy()
            if closest_position:
                enhanced_record["latitude"] = closest_position["latitude"]
                enhanced_record["longitude"] = closest_position["longitude"]
                enhanced_record["lat_e7"] = closest_position.get("lat_e7")
                enhanced_record["lng_e7"] = closest_position.get("lng_e7")
                enhanced_record["accuracy_m"] = closest_position["accuracy_m"]
                enhanced_record["gps_source"] = closest_position["source"]
                enhanced_record["time_to_gps"] = min_time_diff.total_seconds()
            else:
                enhanced_record["gps_source"] = None
                enhanced_record["time_to_gps"] = None

            enhanced_records.append(enhanced_record)

        # Also add position-only records (GPS without activity data)
        for position in positions:
            # Check if this position is already matched
            already_matched = any(
                abs(record.get("latitude", 0) - position["latitude"]) < 0.0000001
                and abs(record.get("longitude", 0) - position["longitude"]) < 0.0000001
                for record in enhanced_records
                if record.get("latitude") and record.get("longitude")
            )

            if not already_matched:
                pos_record = {
                    "edit_index": position["edit_index"],
                    "timestamp": position["timestamp"],
                    "device_id": position["device_id"],
                    "signal_type": "position_only",
                    "primary_activity": "GPS_ONLY",
                    "primary_probability": None,
                    "latitude": position["latitude"],
                    "longitude": position["longitude"],
                    "lat_e7": position.get("lat_e7"),
                    "lng_e7": position.get("lng_e7"),
                    "accuracy_m": position["accuracy_m"],
                    "gps_source": position["source"],
                    "time_to_gps": 0,
                    "all_activities": [],
                    "additional_timestamp": position.get("additional_timestamp"),
                }
                enhanced_records.append(pos_record)

        # Sort by timestamp
        enhanced_records.sort(key=lambda x: x["timestamp"])

        print(
            f"Created {len(enhanced_records)} enhanced records with activity+GPS correlation"
        )
        return enhanced_records

    def analyze_enhanced_data(self, enhanced_records):
        """Analyze the enhanced activity+GPS data"""
        print(f"\n=== ENHANCED TIMELINE ANALYSIS ===")
        print(f"Total records: {len(enhanced_records)}")

        if not enhanced_records:
            print("No data to analyze")
            return

        # Show date range
        start_date = enhanced_records[0]["timestamp"].strftime("%Y-%m-%d %H:%M")
        end_date = enhanced_records[-1]["timestamp"].strftime("%Y-%m-%d %H:%M")
        total_hours = (
            enhanced_records[-1]["timestamp"] - enhanced_records[0]["timestamp"]
        ).total_seconds() / 3600
        print(f"Data period: {start_date} to {end_date} ({total_hours:.1f} hours)")

        # Activity analysis
        activity_counts = defaultdict(int)
        gps_quality_stats = {
            "with_gps": 0,
            "without_gps": 0,
            "total_accuracy": 0,
            "gps_count": 0,
        }

        for record in enhanced_records:
            activity = record.get("primary_activity", "UNKNOWN")
            activity_counts[activity] += 1

            if record.get("latitude") and record.get("longitude"):
                gps_quality_stats["with_gps"] += 1
                accuracy = record.get("accuracy_m", 0)
                if accuracy > 0:
                    gps_quality_stats["total_accuracy"] += accuracy
                    gps_quality_stats["gps_count"] += 1
            else:
                gps_quality_stats["without_gps"] += 1

        print(f"\n=== ACTIVITY SUMMARY ===")
        total_records = len(enhanced_records)
        for activity, count in sorted(
            activity_counts.items(), key=lambda x: x[1], reverse=True
        ):
            percentage = (count / total_records) * 100
            print(f"{activity}: {count} records ({percentage:.1f}%)")

        print(f"\n=== GPS DATA QUALITY ===")
        print(
            f"Records with GPS: {gps_quality_stats['with_gps']}/{total_records} ({gps_quality_stats['with_gps'] / total_records * 100:.1f}%)"
        )
        print(f"Records without GPS: {gps_quality_stats['without_gps']}")

        if gps_quality_stats["gps_count"] > 0:
            avg_accuracy = (
                gps_quality_stats["total_accuracy"] / gps_quality_stats["gps_count"]
            )
            print(f"Average GPS accuracy: {avg_accuracy:.0f} meters")

        # Movement analysis
        self.analyze_movement_with_gps(enhanced_records)

    def analyze_movement_with_gps(self, enhanced_records):
        """Analyze movement patterns using GPS data"""
        print(f"\n=== MOVEMENT ANALYSIS WITH GPS ===")

        # Filter records with GPS data
        gps_records = [
            r
            for r in enhanced_records
            if r.get("latitude")
            and r.get("longitude")
            and r.get("accuracy_m", 1000) < 100
        ]

        if len(gps_records) < 2:
            print("Not enough GPS data for movement analysis")
            return

        print(f"Using {len(gps_records)} GPS records for movement analysis")

        total_distance = 0
        movements = []

        for i in range(1, len(gps_records)):
            prev_record = gps_records[i - 1]
            curr_record = gps_records[i]

            # Calculate distance
            distance = self.haversine_distance(
                prev_record["latitude"],
                prev_record["longitude"],
                curr_record["latitude"],
                curr_record["longitude"],
            )

            # Calculate time difference
            time_diff = (
                curr_record["timestamp"] - prev_record["timestamp"]
            ).total_seconds()

            if distance > 5 and time_diff > 0 and time_diff < 3600:  # Filter noise
                speed = distance / time_diff  # m/s

                if speed < 50:  # Reasonable speed limit
                    total_distance += distance

                    movement = {
                        "timestamp": curr_record["timestamp"],
                        "distance": distance,
                        "time_diff": time_diff,
                        "speed_ms": speed,
                        "speed_kmh": speed * 3.6,
                        "activity": curr_record.get("primary_activity", "UNKNOWN"),
                        "probability": curr_record.get("primary_probability", 0),
                        "start_lat": prev_record["latitude"],
                        "start_lng": prev_record["longitude"],
                        "end_lat": curr_record["latitude"],
                        "end_lng": curr_record["longitude"],
                    }
                    movements.append(movement)

        if movements:
            print(
                f"Total distance traveled: {total_distance:.0f} meters ({total_distance / 1000:.2f} km)"
            )
            print(f"Number of movements: {len(movements)}")

            # Speed analysis by activity
            activity_speeds = defaultdict(list)
            for movement in movements:
                activity_speeds[movement["activity"]].append(movement["speed_kmh"])

            print(f"\nSpeed analysis by activity:")
            for activity, speeds in activity_speeds.items():
                if speeds:
                    avg_speed = sum(speeds) / len(speeds)
                    max_speed = max(speeds)
                    print(
                        f"  {activity}: avg {avg_speed:.1f} km/h, max {max_speed:.1f} km/h ({len(speeds)} movements)"
                    )

            # Show top movements
            print(f"\nTop 10 longest movements:")
            top_movements = sorted(
                movements, key=lambda x: x["distance"], reverse=True
            )[:10]
            for i, movement in enumerate(top_movements, 1):
                time_str = movement["timestamp"].strftime("%Y-%m-%d %H:%M")
                distance = movement["distance"]
                speed = movement["speed_kmh"]
                activity = movement["activity"]
                print(
                    f"  {i}. {time_str}: {distance:.0f}m at {speed:.1f} km/h ({activity})"
                )
        else:
            print("No significant movements detected")

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """Calculate the great circle distance between two points on Earth (in meters)"""
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.asin(math.sqrt(a))

        r = 6371000  # Earth's radius in meters
        return c * r

    def export_enhanced_csv(self, enhanced_records, filename="timeline_enhanced.csv"):
        """Export enhanced data with properly formatted GPS coordinates and distance calculations to CSV"""
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "timestamp",
                "date",
                "time",
                "primary_activity",
                "probability",
                "latitude",
                "longitude",
                "lat_e7_original",
                "lng_e7_original",
                "distance_to_prev_m",
                "accuracy_m",
                "gps_source",
                "time_to_gps_seconds",
                "device_id",
                "signal_type",
                "all_activities_json",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            prev_lat = None
            prev_lng = None

            for i, record in enumerate(enhanced_records):
                timestamp = record["timestamp"]

                # Format coordinates with proper precision
                lat_str = (
                    f"{record.get('latitude', ''):.7f}"
                    if record.get("latitude")
                    else ""
                )
                lng_str = (
                    f"{record.get('longitude', ''):.7f}"
                    if record.get("longitude")
                    else ""
                )

                # Calculate distance to previous position
                distance_to_prev = ""
                current_lat = record.get("latitude")
                current_lng = record.get("longitude")

                if current_lat and current_lng:
                    if prev_lat is not None and prev_lng is not None:
                        distance = self.haversine_distance(
                            prev_lat, prev_lng, current_lat, current_lng
                        )
                        distance_to_prev = f"{distance:.1f}"
                    else:
                        distance_to_prev = "0.0"  # First GPS point

                    prev_lat = current_lat
                    prev_lng = current_lng

                # Get original E7 values
                lat_e7_original = (
                    str(record.get("lat_e7", "")) if record.get("lat_e7") else ""
                )
                lng_e7_original = (
                    str(record.get("lng_e7", "")) if record.get("lng_e7") else ""
                )

                writer.writerow(
                    {
                        "timestamp": timestamp.isoformat(),
                        "date": timestamp.strftime("%Y-%m-%d"),
                        "time": timestamp.strftime("%H:%M:%S"),
                        "primary_activity": record.get("primary_activity", ""),
                        "probability": record.get("primary_probability", ""),
                        "latitude": lat_str,
                        "longitude": lng_str,
                        "lat_e7_original": lat_e7_original,
                        "lng_e7_original": lng_e7_original,
                        "distance_to_prev_m": distance_to_prev,
                        "accuracy_m": record.get("accuracy_m", ""),
                        "gps_source": record.get("gps_source", ""),
                        "time_to_gps_seconds": record.get("time_to_gps", ""),
                        "device_id": record.get("device_id", ""),
                        "signal_type": record.get("signal_type", ""),
                        "all_activities_json": json.dumps(
                            record.get("all_activities", [])
                        ),
                    }
                )

        print(
            f"\nEnhanced data with GPS coordinates, E7 values, and distances exported to {filename}"
        )

    def filter_by_date(self, enhanced_records, date_filter):
        """Filter data by date"""
        print(f"Filtering data for: {date_filter}")

        try:
            if len(date_filter) == 10:  # YYYY-MM-DD
                filter_date = datetime.strptime(date_filter, "%Y-%m-%d").date()
                filtered_records = [
                    r for r in enhanced_records if r["timestamp"].date() == filter_date
                ]
            elif len(date_filter) == 7:  # YYYY-MM
                filter_year, filter_month = map(int, date_filter.split("-"))
                filtered_records = [
                    r
                    for r in enhanced_records
                    if r["timestamp"].year == filter_year
                    and r["timestamp"].month == filter_month
                ]
            else:
                print("Invalid date format. Use YYYY-MM-DD or YYYY-MM")
                return enhanced_records

            print(f"Filtered to {len(filtered_records)} records")
            return filtered_records

        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD or YYYY-MM")
            return enhanced_records


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Parse Google Timeline Edits with fixed GPS coordinate handling and distance calculations"
    )
    parser.add_argument(
        "path", help="Path to Timeline JSON file or directory containing Timeline files"
    )
    parser.add_argument(
        "--export-csv",
        action="store_true",
        help="Export to CSV file with GPS data and distance calculations",
    )
    parser.add_argument(
        "--date-filter", help="Filter by date (YYYY-MM-DD or YYYY-MM)", default=None
    )

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} not found!")
        return

    print("Google Timeline Edits Parser (Complete Version with Distance Tracking)")
    print("=======================================================================")

    # Initialize parser
    timeline_parser = TimelineEditsParser(args.path)

    # Load data
    if not timeline_parser.load_timeline_edits():
        return

    # Parse all signals
    activities, positions, wifi_scans = timeline_parser.parse_all_signals()

    # Correlate activities with GPS positions
    enhanced_records = timeline_parser.correlate_activities_with_positions(
        activities, positions
    )

    # Apply date filter if specified
    if args.date_filter:
        enhanced_records = timeline_parser.filter_by_date(
            enhanced_records, args.date_filter
        )

    # Analyze enhanced data
    timeline_parser.analyze_enhanced_data(enhanced_records)

    # Export if requested
    if args.export_csv:
        timeline_parser.export_enhanced_csv(enhanced_records)


if __name__ == "__main__":
    main()
