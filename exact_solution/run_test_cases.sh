#!/bin/bash

# Assuming your Python script is named "your_python_script.py"
PYTHON_SCRIPT="exact_solution.py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Error: $PYTHON_SCRIPT not found!"
  exit 1
fi

# Directory containing test input files
TEST_INPUT_DIR="./test_cases/inputs"

# Directory containing expected output files
EXPECTED_OUTPUT_DIR="./test_cases/outputs"

# Check if the test input directory exists
if [ ! -d "$TEST_INPUT_DIR" ]; then
  echo "Error: Test input directory $TEST_INPUT_DIR not found!"
  exit 1
fi

# Check if the expected output directory exists
if [ ! -d "$EXPECTED_OUTPUT_DIR" ]; then
  echo "Error: Expected output directory $EXPECTED_OUTPUT_DIR not found!"
  exit 1
fi

# Get a list of all text files in the test input directory
TEST_FILES=$(ls "$TEST_INPUT_DIR"/*.txt)

# Check if there are any test input files
if [ -z "$TEST_FILES" ]; then
  echo "Error: No test input files found in $TEST_INPUT_DIR!"
  exit 1
fi

# Iterate over each test input file
for TEST_FILE in $TEST_FILES; do
  # Prepare the expected output file path
  EXPECTED_OUTPUT_FILE="$EXPECTED_OUTPUT_DIR/$(basename "$TEST_FILE" .txt)_expected.txt"

  # Check if the expected output file exists
  if [ ! -f "$EXPECTED_OUTPUT_FILE" ]; then
    echo "Error: Expected output file $EXPECTED_OUTPUT_FILE not found!"
    exit 1
  fi

  # Run the Python script and measure the execution time
  
  echo "-------------------------------"
  echo "Running test for $TEST_FILE..."
  echo " "
  TIME_START=$(date +%s.%N)

  TEMP_OUTPUT_FILE=$(mktemp)
  python "$PYTHON_SCRIPT" < "$TEST_FILE" > "$TEMP_OUTPUT_FILE"
  TIME_END=$(date +%s.%N)
  ELAPSED_TIME=$(echo "$TIME_END - $TIME_START" | bc)

  # Compare the actual output with the expected output
  if ! diff -q "$TEMP_OUTPUT_FILE" "$EXPECTED_OUTPUT_FILE" > /dev/null; then
    echo "Test failed for $TEST_FILE"
    echo "Differences:"
    diff "$TEMP_OUTPUT_FILE" "$EXPECTED_OUTPUT_FILE"
  else
    echo "Test passed for $TEST_FILE (Time: ${ELAPSED_TIME}s)"
  fi

  # Clean up the temporary output file
  rm "$TEMP_OUTPUT_FILE"
done
