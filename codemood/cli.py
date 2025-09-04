"""
Command-line interface for codemood package.
"""

import argparse
import sys
import subprocess
import requests
from typing import Optional
from . import __version__

try:
    from importlib.metadata import version as _version
except ImportError:
    try:
        from importlib_metadata import version as _version  # type: ignore
    except ImportError:
        _version = None


def get_current_version() -> str:
    """Get the current installed version of codemood."""
    if _version is not None:
        try:
            return _version("codemood")  # type: ignore
        except Exception:
            pass
    return __version__


def get_latest_version() -> Optional[str]:
    """Get the latest version from PyPI."""
    try:
        response = requests.get("https://pypi.org/pypi/codemood/json", timeout=5)
        if response.status_code == 200:
            return response.json()["info"]["version"]
    except Exception:
        pass
    return None


def check_version() -> None:
    """Check current version and compare with latest."""
    current = get_current_version()
    print(f"Current version: {current}")

    latest = get_latest_version()
    if latest:
        print(f"Latest version: {latest}")
        if current != latest:
            print("Update available! Run 'codemood --update' to upgrade.")
        else:
            print("You have the latest version!")
    else:
        print("Could not check for updates (network error)")


def update_package() -> None:
    """Update codemood to the latest version."""
    try:
        print("Updating codemood...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "codemood"]
        )
        print("Successfully updated codemood!")
    except subprocess.CalledProcessError:
        print("Failed to update. Try: pip install --upgrade codemood")


def show_info() -> None:
    """Show package information."""
    current = get_current_version()
    print(
        f"""
Codemood v{current}
Advanced code analysis platform with AI sentiment analysis

Features:
• Advanced sentiment analysis with emotional tone detection
• Performance optimization suggestions
• Security vulnerability scanning
• Comprehensive code quality metrics
• Custom model training pipeline

Usage:
  from codemood import analyze_sentiment_advanced
  result = analyze_sentiment_advanced(code)

Documentation: https://github.com/OmkarPalika/codemood
"""
    )


def analyze_file(filepath: str) -> None:
    """Analyze a code file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        from . import analyze_sentiment_advanced

        result = analyze_sentiment_advanced(code)

        print(f"\nAnalysis for: {filepath}")
        print(f"Overall Score: {result.overall_score:.2f}")
        print(f"Emotional Tone: {result.emotional_tone}")
        print(f"Confidence: {result.confidence:.2f}")

        if result.reasoning:
            print("\nReasons:")
            for reason in result.reasoning[:3]:  # Show top 3 reasons
                print(f"  • {reason}")

    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except Exception as e:
        print(f"Error analyzing file: {e}")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="codemood",
        description="Advanced code analysis platform with AI sentiment analysis",
    )

    parser.add_argument(
        "-v", "--version", action="store_true", help="Show current version"
    )
    parser.add_argument("-c", "--check", action="store_true", help="Check for updates")
    parser.add_argument(
        "-u", "--update", action="store_true", help="Update to latest version"
    )
    parser.add_argument(
        "-i", "--info", action="store_true", help="Show package information"
    )
    parser.add_argument("-a", "--analyze", metavar="FILE", help="Analyze a code file")

    args = parser.parse_args()

    if args.version:
        print(get_current_version())
        sys.exit(0)
    elif args.check:
        check_version()
        sys.exit(0)
    elif args.update:
        update_package()
        sys.exit(0)
    elif args.info:
        show_info()
        sys.exit(0)
    elif args.analyze:
        analyze_file(args.analyze)
        sys.exit(0)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
