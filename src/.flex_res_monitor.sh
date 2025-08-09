#!/bin/bash

# Flexible process monitor - specify your own patterns
# Usage: ./flexible_monitor.sh

# Configuration - modify these patterns based on your actual processes
JAVA_PATTERNS=("java" "openjdk" "\.jar" "tomcat" "eclipse" "intellij" "netbeans" "maven" "gradle")
PYTHON_PATTERNS=("python3" "python" "\.py")

# Function to find processes by multiple patterns
find_processes_by_patterns() {
    local patterns=("$@")
    local found_pids=""
    
    for pattern in "${patterns[@]}"; do
        local pids=$(pgrep -f "$pattern" 2>/dev/null)
        if [ ! -z "$pids" ]; then
            found_pids="$found_pids $pids"
        fi
    done
    
    # Remove duplicates and return unique PIDs
    echo "$found_pids" | tr ' ' '\n' | sort -u | tr '\n' ' '
}

# Function to monitor processes
monitor_processes() {
    local process_type=$1
    local output_file="${process_type}.res.txt"
    shift
    local patterns=("$@")
    
    echo "Timestamp,PID,RES_KB,VSZ_KB,CPU%,Command" > "$output_file"
    
    while true; do
        timestamp=$(date '+%Y-%m-%d %H:%M:%S')
        pids=$(find_processes_by_patterns "${patterns[@]}")
        
        if [ ! -z "$pids" ]; then
            for pid in $pids; do
                if kill -0 $pid 2>/dev/null; then
                    # Get detailed process info
                    ps_line=$(ps -p $pid -o pid=,rss=,vsz=,pcpu=,cmd= 2>/dev/null)
                    if [ ! -z "$ps_line" ]; then
                        echo "$timestamp,$ps_line" >> "$output_file"
                    fi
                fi
            done
        else
            # Only log "not found" every 30 seconds to reduce noise
            if [ $(($(date +%s) % 30)) -eq 0 ]; then
                echo "$timestamp,N/A,0,0,0,No $process_type process found (patterns: ${patterns[*]})" >> "$output_file"
            fi
        fi
        
        sleep 1
    done
}

# Cleanup function
cleanup() {
    echo -e "\nStopping monitoring..."
    kill $(jobs -p) 2>/dev/null
    echo "Final process counts:"
    echo "Java processes logged: $(tail -n +2 java.res.txt 2>/dev/null | grep -v "N/A" | wc -l)"
    echo "Python processes logged: $(tail -n +2 python3.res.txt 2>/dev/null | grep -v "N/A" | wc -l)"
    exit 0
}

trap cleanup SIGINT SIGTERM

echo "=== Flexible Process Monitor ==="
echo "Monitoring patterns..."
echo "Java patterns: ${JAVA_PATTERNS[*]}"
echo "Python patterns: ${PYTHON_PATTERNS[*]}"
echo ""
echo "Output files: java.res.txt, python3.res.txt"
echo "Press Ctrl+C to stop"
echo ""

# Initial check
echo "Initial process check:"
java_pids=$(find_processes_by_patterns "${JAVA_PATTERNS[@]}")
python_pids=$(find_processes_by_patterns "${PYTHON_PATTERNS[@]}")

echo "Found Java PIDs: ${java_pids:-none}"
echo "Found Python PIDs: ${python_pids:-none}"
echo ""

if [ -z "$java_pids" ] && [ -z "$python_pids" ]; then
    echo "WARNING: No processes found matching the patterns!"
    echo "Consider running the diagnostic script first or starting some Java/Python processes."
    echo ""
    read -p "Continue monitoring anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 0
    fi
fi

echo "Starting monitoring..."

# Start monitoring in background
monitor_processes "java" "${JAVA_PATTERNS[@]}" &
monitor_processes "python3" "${PYTHON_PATTERNS[@]}" &

# Wait for background jobs
wait