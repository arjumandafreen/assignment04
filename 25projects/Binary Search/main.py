import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Function to perform binary search and yield steps
def binary_search_steps(arr, target):
    steps = []
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high))
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return steps

# Function to plot the current step with enhanced visuals
def plot_step(arr, low, mid, high):
    colors = ['lightgray'] * len(arr)  # Background color for all bars
    if low < len(arr):
        colors[low] = 'green'  # Green for low index
    if mid < len(arr):
        colors[mid] = 'blue'  # Blue for mid index
    if high < len(arr):
        colors[high] = 'red'  # Red for high index

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', width=0.8)

    # Adding text labels for clarity
    for i, value in enumerate(arr):
        ax.text(i, value + 0.5, str(value), ha='center', va='bottom', fontsize=10)

    ax.set_xticks(range(len(arr)))
    ax.set_xticklabels(arr)
    ax.set_title("Binary Search Step", fontsize=16)
    ax.set_ylabel("Value", fontsize=12)
    ax.set_xlabel("Index", fontsize=12)

    # Improve layout for readability
    plt.tight_layout()
    st.pyplot(fig)

# Streamlit app
st.title("🔍 Binary Search Visualizer")
st.markdown("Visualize how the **binary search** algorithm works step by step. Enter a sorted list of numbers and a target to see the process in action.")

# User inputs with error handling for a better experience
array_input = st.text_input("Enter a sorted list of numbers (comma-separated):", "1,3,5,7,9,11,13,15")
target_input = st.number_input("Enter the target number:", value=7)

# Convert input string to list of integers with error handling
try:
    arr = list(map(int, array_input.strip().split(',')))
    arr.sort()
    if len(arr) < 2:
        st.warning("Please enter at least two numbers in the list.")
        st.stop()
except:
    st.error("Please enter a valid list of numbers.")
    st.stop()

# Run binary search and visualize steps when the button is pressed
if st.button("Run Binary Search"):
    if not arr:
        st.error("Array is empty. Please enter a valid list of numbers.")
        st.stop()
    
    steps = binary_search_steps(arr, target_input)
    
    # Display a success message if target is found
    target_found = False
    for low, mid, high in steps:
        plot_step(arr, low, mid, high)
        time.sleep(1)  # Pause for a second between steps
        if arr[mid] == target_input:
            target_found = True

    if target_found:
        st.success(f"Target {target_input} found in the array!")
    else:
        st.warning(f"Target {target_input} not found in the array.")

