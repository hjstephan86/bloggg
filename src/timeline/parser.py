#!/usr/bin/env python3
"""
Google Timeline Semantic Segments Parser
Parses the new semantic segments format with activities, visits, and positions
"""

import argparse
import json
import math
import os
from collections import defaultdict
from datetime import datetime, timedelta
import re


class TimelineSemanticParser:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.semantic_segments = []

    def load_timeline_data(self, file_path=None):
        """Load timeline data from JSON file"""
        if file_path:
            self.file_path = file_path

        if not self.file_path:
            raise ValueError("No file path provided")

        if not os.path.isfile(self.file_path):
            print(f"Error: {self.file_path} is not a valid file!")
            return False

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                if "semanticSegments" in data:
                    self.semantic_segments = data["semanticSegments"]
                    print(f"Loaded {len(self.semantic_segments)} semantic segments")
                    return True
                else:
                    print("No 'semanticSegments' found in JSON file")
                    return False

        except Exception as e:
            print(f"Error reading {self.file_path}: {e}")
            return False

    def parse_latlng_string(self, latlng_str):
        """Parse LatLng string format '52.0187241°, 8.5751769°' to decimal degrees"""
        if not latlng_str:
            return None, None
        
        try:
            # Remove degree symbols and split
            clean_str = latlng_str.replace('°', '').strip()
            parts = clean_str.split(',')
            if len(parts) == 2:
                lat = float(parts[0].strip())
                lng = float(parts[1].strip())
                return lat, lng
        except Exception as e:
            print(f"Error parsing LatLng '{latlng_str}': {e}")
        
        return None, None

    def parse_all_segments(self):
        """Parse all semantic segments into structured records"""
        records = []

        for i, segment in enumerate(self.semantic_segments):
            # Parse activity segments
            if "activity" in segment:
                record = self._parse_activity_segment(segment, i)
                if record:
                    records.append(record)

            # Parse visit segments
            elif "visit" in segment:
                record = self._parse_visit_segment(segment, i)
                if record:
                    records.append(record)

            # Parse standalone position records
            elif "position" in segment:
                record = self._parse_position_record(segment, i)
                if record:
                    records.append(record)

            # Parse standalone activity records
            elif "activityRecord" in segment:
                record = self._parse_activity_record(segment, i)
                if record:
                    records.append(record)

            # Parse wifi scans
            elif "wifiScan" in segment:
                record = self._parse_wifi_scan(segment, i)
                if record:
                    records.append(record)

        # Sort by timestamp
        records.sort(key=lambda x: x["timestamp"])

        print(f"\nParsed {len(records)} total records:")
        type_counts = defaultdict(int)
        for r in records:
            type_counts[r["record_type"]] += 1
        for rtype, count in type_counts.items():
            print(f"  {rtype}: {count}")

        return records

    def _parse_activity_segment(self, segment, index):
        """Parse activity segment (movement)"""
        activity_data = segment["activity"]
        start_time_str = segment.get("startTime")
        end_time_str = segment.get("endTime")

        if not start_time_str:
            return None

        try:
            start_time = datetime.fromisoformat(start_time_str.replace("Z", "+00:00"))
            end_time = datetime.fromisoformat(end_time_str.replace("Z", "+00:00")) if end_time_str else start_time

            # Parse start and end locations
            start_lat, start_lng = None, None
            end_lat, end_lng = None, None

            if "start" in activity_data and "latLng" in activity_data["start"]:
                start_lat, start_lng = self.parse_latlng_string(activity_data["start"]["latLng"])

            if "end" in activity_data and "latLng" in activity_data["end"]:
                end_lat, end_lng = self.parse_latlng_string(activity_data["end"]["latLng"])

            # Get activity type
            top_candidate = activity_data.get("topCandidate", {})
            activity_type = top_candidate.get("type", "UNKNOWN")
            probability = top_candidate.get("probability", 0)

            record = {
                "segment_index": index,
                "timestamp": start_time,
                "end_timestamp": end_time,
                "record_type": "activity",
                "activity_type": activity_type,
                "probability": probability,
                "start_latitude": start_lat,
                "start_longitude": start_lng,
                "end_latitude": end_lat,
                "end_longitude": end_lng,
                "distance_meters": activity_data.get("distanceMeters"),
                "duration_seconds": (end_time - start_time).total_seconds(),
                "place_id": None,
                "semantic_type": None,
            }

            return record

        except Exception as e:
            print(f"Error parsing activity segment {index}: {e}")
            return None

    def _parse_visit_segment(self, segment, index):
        """Parse visit segment (stay at location)"""
        visit_data = segment["visit"]
        start_time_str = segment.get("startTime")
        end_time_str = segment.get("endTime")

        if not start_time_str:
            return None

        try:
            start_time = datetime.fromisoformat(start_time_str.replace("Z", "+00:00"))
            end_time = datetime.fromisoformat(end_time_str.replace("Z", "+00:00")) if end_time_str else start_time

            # Get location from top candidate
            top_candidate = visit_data.get("topCandidate", {})
            place_location = top_candidate.get("placeLocation", {})
            
            lat, lng = None, None
            if "latLng" in place_location:
                lat, lng = self.parse_latlng_string(place_location["latLng"])

            record = {
                "segment_index": index,
                "timestamp": start_time,
                "end_timestamp": end_time,
                "record_type": "visit",
                "activity_type": "VISIT",
                "probability": visit_data.get("probability", 0),
                "start_latitude": lat,
                "start_longitude": lng,
                "end_latitude": lat,
                "end_longitude": lng,
                "distance_meters": 0,
                "duration_seconds": (end_time - start_time).total_seconds(),
                "place_id": top_candidate.get("placeId"),
                "semantic_type": top_candidate.get("semanticType", "UNKNOWN"),
            }

            return record

        except Exception as e:
            print(f"Error parsing visit segment {index}: {e}")
            return None

    def _parse_position_record(self, segment, index):
        """Parse standalone position record"""
        position_data = segment["position"]
        timestamp_str = position_data.get("timestamp")

        if not timestamp_str:
            return None

        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))

            lat, lng = None, None
            if "LatLng" in position_data:
                lat, lng = self.parse_latlng_string(position_data["LatLng"])

            record = {
                "segment_index": index,
                "timestamp": timestamp,
                "end_timestamp": timestamp,
                "record_type": "position",
                "activity_type": "GPS_POSITION",
                "probability": None,
                "start_latitude": lat,
                "start_longitude": lng,
                "end_latitude": lat,
                "end_longitude": lng,
                "distance_meters": 0,
                "duration_seconds": 0,
                "place_id": None,
                "semantic_type": None,
                "accuracy_meters": position_data.get("accuracyMeters"),
                "altitude_meters": position_data.get("altitudeMeters"),
                "source": position_data.get("source"),
                "speed_mps": position_data.get("speedMetersPerSecond"),
            }

            return record

        except Exception as e:
            print(f"Error parsing position record {index}: {e}")
            return None

    def _parse_activity_record(self, segment, index):
        """Parse standalone activity record"""
        activity_data = segment["activityRecord"]
        timestamp_str = activity_data.get("timestamp")

        if not timestamp_str:
            return None

        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))

            # Get most probable activity
            probable_activities = activity_data.get("probableActivities", [])
            if probable_activities:
                top_activity = max(probable_activities, key=lambda x: x.get("confidence", 0))
                activity_type = top_activity.get("type", "UNKNOWN")
                confidence = top_activity.get("confidence", 0)
            else:
                activity_type = "UNKNOWN"
                confidence = 0

            record = {
                "segment_index": index,
                "timestamp": timestamp,
                "end_timestamp": timestamp,
                "record_type": "activity_record",
                "activity_type": activity_type,
                "probability": confidence,
                "start_latitude": None,
                "start_longitude": None,
                "end_latitude": None,
                "end_longitude": None,
                "distance_meters": 0,
                "duration_seconds": 0,
                "place_id": None,
                "semantic_type": None,
            }

            return record

        except Exception as e:
            print(f"Error parsing activity record {index}: {e}")
            return None

    def _parse_wifi_scan(self, segment, index):
        """Parse wifi scan record"""
        wifi_data = segment["wifiScan"]
        timestamp_str = wifi_data.get("deliveryTime")

        if not timestamp_str:
            return None

        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))

            devices = wifi_data.get("devicesRecords", [])
            strongest_signal = max([d.get("rawRssi", -100) for d in devices]) if devices else None

            record = {
                "segment_index": index,
                "timestamp": timestamp,
                "end_timestamp": timestamp,
                "record_type": "wifi_scan",
                "activity_type": "WIFI_SCAN",
                "probability": None,
                "start_latitude": None,
                "start_longitude": None,
                "end_latitude": None,
                "end_longitude": None,
                "distance_meters": 0,
                "duration_seconds": 0,
                "place_id": None,
                "semantic_type": None,
                "wifi_devices": len(devices),
                "strongest_signal": strongest_signal,
            }

            return record

        except Exception as e:
            print(f"Error parsing wifi scan {index}: {e}")
            return None

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """Calculate distance between two points in meters"""
        if None in [lat1, lon1, lat2, lon2]:
            return 0

        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return c * 6371000  # Earth's radius in meters

    def analyze_timeline(self, records):
        """Analyze the parsed timeline data"""
        print(f"\n=== TIMELINE ANALYSIS ===")
        print(f"Total records: {len(records)}")

        if not records:
            return

        # Date range
        start_date = records[0]["timestamp"].strftime("%Y-%m-%d %H:%M")
        end_date = records[-1]["timestamp"].strftime("%Y-%m-%d %H:%M")
        total_hours = (records[-1]["timestamp"] - records[0]["timestamp"]).total_seconds() / 3600
        print(f"Period: {start_date} to {end_date} ({total_hours:.1f} hours)")

        # Activity breakdown with distances
        activity_counts = defaultdict(int)
        activity_distances = defaultdict(float)
        total_distance = 0
        
        for record in records:
            activity_counts[record["activity_type"]] += 1
            if record.get("distance_meters"):
                distance = record["distance_meters"]
                activity_distances[record["activity_type"]] += distance
                total_distance += distance

        print(f"\n=== ACTIVITY BREAKDOWN ===")
        for activity, count in sorted(activity_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / len(records)) * 100
            distance = activity_distances.get(activity, 0)
            if distance > 0:
                print(f"{activity}: {count} records ({percentage:.1f}%) - {distance:.1f}m ({distance/1000:.2f}km)")
            else:
                print(f"{activity}: {count} records ({percentage:.1f}%)")

        print(f"\n=== TOTAL DISTANCE ===")
        print(f"Overall: {total_distance:.1f} meters ({total_distance / 1000:.2f} km)")
        
        if activity_distances:
            print(f"\nDistance by activity type:")
            for activity, distance in sorted(activity_distances.items(), key=lambda x: x[1], reverse=True):
                percentage = (distance / total_distance * 100) if total_distance > 0 else 0
                print(f"  {activity}: {distance:.1f}m ({distance/1000:.2f}km) - {percentage:.1f}% of total")

        # Location records
        location_records = [r for r in records if r["start_latitude"] is not None]
        print(f"\n=== LOCATION DATA ===")
        print(f"Records with location data: {len(location_records)}/{len(records)} ({len(location_records) / len(records) * 100:.1f}%)")

    def export_csv(self, records, filename="timeline_semantic.csv"):
        """Export records to CSV"""
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "timestamp",
                "end_timestamp",
                "date",
                "time",
                "record_type",
                "activity_type",
                "probability",
                "start_latitude",
                "start_longitude",
                "end_latitude",
                "end_longitude",
                "distance_meters",
                "duration_seconds",
                "place_id",
                "semantic_type",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()

            for record in records:
                row = {
                    "timestamp": record["timestamp"].isoformat(),
                    "end_timestamp": record["end_timestamp"].isoformat() if record.get("end_timestamp") else "",
                    "date": record["timestamp"].strftime("%Y-%m-%d"),
                    "time": record["timestamp"].strftime("%H:%M:%S"),
                    "record_type": record.get("record_type", ""),
                    "activity_type": record.get("activity_type", ""),
                    "probability": f"{record['probability']:.4f}" if record.get("probability") is not None else "",
                    "start_latitude": f"{record['start_latitude']:.7f}" if record.get("start_latitude") is not None else "",
                    "start_longitude": f"{record['start_longitude']:.7f}" if record.get("start_longitude") is not None else "",
                    "end_latitude": f"{record['end_latitude']:.7f}" if record.get("end_latitude") is not None else "",
                    "end_longitude": f"{record['end_longitude']:.7f}" if record.get("end_longitude") is not None else "",
                    "distance_meters": f"{record['distance_meters']:.1f}" if record.get("distance_meters") is not None else "",
                    "duration_seconds": f"{record['duration_seconds']:.0f}" if record.get("duration_seconds") is not None else "",
                    "place_id": record.get("place_id", ""),
                    "semantic_type": record.get("semantic_type", ""),
                }
                writer.writerow(row)

        print(f"\nData exported to {filename}")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Parse Google Timeline Semantic Segments format"
    )
    parser.add_argument("path", help="Path to Timeline JSON file")
    parser.add_argument("--export-csv", action="store_true", help="Export to CSV file")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} not found!")
        return

    print("Google Timeline Semantic Segments Parser")
    print("=" * 50)

    # Initialize parser
    timeline_parser = TimelineSemanticParser(args.path)

    # Load data
    if not timeline_parser.load_timeline_data():
        return

    # Parse segments
    records = timeline_parser.parse_all_segments()

    # Analyze
    timeline_parser.analyze_timeline(records)

    # Export if requested
    if args.export_csv:
        timeline_parser.export_csv(records)


if __name__ == "__main__":
    main()
