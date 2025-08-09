"""
Lines of code (loc) analyzer that scans files recursively in a folder and provides detailed
statistics about different types of code lines across multiple programming languages.

Categorizes lines into three types:
- Blank: Empty lines or lines containing only whitespace
- Comment: Single-line comments, multi-line comments, and docstrings
- Code: Actual executable/functional code lines

Features:
- Recursive directory scanning with support for individual files
- Language-specific comment pattern recognition
- Special Python docstring detection (module, class, and function docstrings)
- Multi-line comment block handling for C-style languages
- Comprehensive statistics with file counts and totals per language
- Tabulated output format for easy readability

Supported file types: .py, .java, .css, .html, .htm, .js, .jsx, .ts, .tsx
Output format: Language | Files | Blank | Comment | Code | Total
"""

import argparse
import re
from collections import defaultdict
from pathlib import Path

from tabulate import tabulate


class CodeAnalyzer:
    def __init__(self):
        # File extensions to language mapping
        self.file_extensions = {
            ".py": "Python",
            ".java": "Java",
            ".css": "CSS",
            ".html": "HTML",
            ".htm": "HTML",
            ".js": "JavaScript",
            ".jsx": "JavaScript",
            ".ts": "JavaScript",
            ".tsx": "JavaScript",
        }

        # Statistics
        self.stats = defaultdict(
            lambda: {"blank": 0, "comment": 0, "code": 0, "files": 0}
        )

    def is_blank_line(self, line):
        """Checks if a line is empty or only whitespace"""
        return len(line.strip()) == 0

    def analyze_python_file(self, file_path):
        """Special handling for Python files to match cloc behavior"""
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        in_docstring = False
        docstring_delimiter = None

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Blank lines
            if not stripped:
                self.stats["Python"]["blank"] += 1
                continue

            # Handle docstring continuation
            if in_docstring:
                if docstring_delimiter in line:
                    # End of docstring
                    self.stats["Python"]["comment"] += 1
                    in_docstring = False
                    docstring_delimiter = None
                else:
                    # Middle of docstring
                    self.stats["Python"]["comment"] += 1
                continue

            # Check for docstring start
            if '"""' in stripped or "'''" in stripped:
                delimiter = '"""' if '"""' in stripped else "'''"

                # Check if it's a complete docstring on one line
                if stripped.count(delimiter) >= 2:
                    # Complete docstring on one line - check if it's really a docstring
                    if self.is_python_docstring(i, lines):
                        self.stats["Python"]["comment"] += 1
                    else:
                        self.stats["Python"]["code"] += 1
                else:
                    # Start of multi-line docstring
                    if self.is_python_docstring(i, lines):
                        self.stats["Python"]["comment"] += 1
                        in_docstring = True
                        docstring_delimiter = delimiter
                    else:
                        self.stats["Python"]["code"] += 1
                continue

            # Single line comment
            if stripped.startswith("#"):
                self.stats["Python"]["comment"] += 1
                continue

            # Regular code line
            self.stats["Python"]["code"] += 1

    def is_python_docstring(self, line_num, lines):
        """Check if a triple-quoted string is actually a docstring"""
        # Look backwards for the defining statement
        for i in range(line_num - 1, -1, -1):
            prev_line = lines[i].strip()
            if not prev_line:
                continue

            # If we find a function/class definition, this is a docstring
            if (
                prev_line.startswith("def ")
                or prev_line.startswith("class ")
                or prev_line.startswith("async def ")
                or prev_line.endswith(":")
            ):
                return True

            # If we find other code, it's not a docstring
            if not prev_line.startswith("#"):
                break

        # Check if it's a module docstring (at the beginning)
        for i in range(line_num):
            check_line = lines[i].strip()
            if check_line and not check_line.startswith("#"):
                return False

        return True

    def analyze_non_python_file(self, file_path, language):
        """Handle non-Python files with standard comment patterns"""
        comment_patterns = {
            "Java": {
                "single": r"^\s*//",
                "multi_start": r"^\s*/\*",
                "multi_end": r"\*/\s*$",
                "multi_single": r"^\s*/\*.*\*/\s*$",
            },
            "JavaScript": {
                "single": r"^\s*//",
                "multi_start": r"^\s*/\*",
                "multi_end": r"\*/\s*$",
                "multi_single": r"^\s*/\*.*\*/\s*$",
            },
            "CSS": {
                "single": None,
                "multi_start": r"^\s*/\*",
                "multi_end": r"\*/\s*$",
                "multi_single": r"^\s*/\*.*\*/\s*$",
            },
            "HTML": {
                "single": None,
                "multi_start": r"^\s*<!--",
                "multi_end": r"-->\s*$",
                "multi_single": r"^\s*<!--.*-->\s*$",
            },
        }

        patterns = comment_patterns.get(language, {})

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        in_multi_comment = False

        for line in lines:
            stripped = line.strip()

            # Blank lines
            if not stripped:
                self.stats[language]["blank"] += 1
                continue

            # Single-line multi-comment
            if patterns.get("multi_single") and re.match(
                patterns["multi_single"], line
            ):
                self.stats[language]["comment"] += 1
                continue

            # Multi-line comment handling
            if in_multi_comment:
                self.stats[language]["comment"] += 1
                if patterns.get("multi_end") and re.search(patterns["multi_end"], line):
                    in_multi_comment = False
                continue

            # Start of multi-line comment
            if patterns.get("multi_start") and re.search(patterns["multi_start"], line):
                self.stats[language]["comment"] += 1
                if not (
                    patterns.get("multi_end") and re.search(patterns["multi_end"], line)
                ):
                    in_multi_comment = True
                continue

            # Single line comment
            if patterns.get("single") and re.match(patterns["single"], line):
                self.stats[language]["comment"] += 1
                continue

            # Code line
            self.stats[language]["code"] += 1

    def analyze_file(self, file_path):
        """Analyzes a single file"""
        try:
            extension = Path(file_path).suffix.lower()
            if extension not in self.file_extensions:
                return

            language = self.file_extensions[extension]

            if language == "Python":
                self.analyze_python_file(file_path)
            else:
                self.analyze_non_python_file(file_path, language)

            self.stats[language]["files"] += 1

        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

    def scan_directory(self, directory):
        """Scans a directory recursively"""
        directory = Path(directory)

        if not directory.exists():
            print(f"Directory {directory} does not exist!")
            return

        # Recursively go through all files
        for file_path in directory.rglob("*"):
            if file_path.is_file():
                self.analyze_file(file_path)

    def print_results(self):
        """Outputs the results as a table"""
        if not self.stats:
            print("No supported files found!")
            return

        # Prepare table data
        table_data = []
        total_blank = total_comment = total_code = total_files = 0

        for language in sorted(self.stats.keys()):
            stats = self.stats[language]
            total_lines = stats["blank"] + stats["comment"] + stats["code"]

            table_data.append(
                [
                    language,
                    stats["files"],
                    stats["blank"],
                    stats["comment"],
                    stats["code"],
                    total_lines,
                ]
            )

            total_blank += stats["blank"]
            total_comment += stats["comment"]
            total_code += stats["code"]
            total_files += stats["files"]

        # Add total row
        total_total = total_blank + total_comment + total_code
        # Add separator and total row
        table_data.append(["-" * 8, "-" * 5, "-" * 5, "-" * 7, "-" * 4, "-" * 5])
        table_data.append(
            ["Total", total_files, total_blank, total_comment, total_code, total_total]
        )

        # Output table
        headers = ["Language", "Files", "Blank", "Comment", "Code", "Total"]
        print(
            tabulate(table_data, headers=headers, tablefmt="simple", numalign="right")
        )


def main():
    parser = argparse.ArgumentParser(
        description="Counts code lines in Python, Java, CSS, HTML, and JavaScript files"
    )
    parser.add_argument("path", help="Directory or file to scan")
    parser.add_argument("-v", "--verbose", action="store_true", help="Detailed print")

    args = parser.parse_args()

    analyzer = CodeAnalyzer()

    # Check if path is a file or directory
    path = Path(args.path)
    if path.is_file():
        analyzer.analyze_file(path)
    elif path.is_dir():
        analyzer.scan_directory(path)
    else:
        print(f"Error: {args.path} is not a valid file or directory!")
        return

    analyzer.print_results()


if __name__ == "__main__":
    main()
