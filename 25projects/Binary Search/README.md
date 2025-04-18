# 🔍 Binary Search Visualizer

This project is a visual demonstration of the **Binary Search Algorithm** using Python and Streamlit. It allows users to input a sorted list and a target value, then watch each step of the search process through colorful visualizations.

## 📽️ Demo Preview

Each iteration of the algorithm is shown using a bar chart:
- 🟩 **Green**: `Low` index
- 🔵 **Blue**: `Mid` index
- 🔴 **Red**: `High` index  
- 🩶 **Gray**: Other elements

This helps users understand how the binary search narrows down the range and homes in on the target.

---

## 🚀 Features

- ✅ Step-by-step visualization of binary search
- 📊 Interactive bar charts with color-coded steps
- ⌛ 1-second pause between each step for better understanding
- 🔢 Accepts any sorted list of integers
- 🎯 User can specify the target number
- 📈 Visual feedback on whether the target was found or not

---

## 🧠 How Binary Search Works

Binary Search works by:
1. Splitting the list in half
2. Checking if the middle element is the target
3. Narrowing the range to the left or right half based on comparison
4. Repeating until the target is found or the range is empty

This app visualizes that process in a friendly and educational way.

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- Matplotlib
- NumPy (optional, but used for better plotting)

Install dependencies:

```bash
pip install streamlit matplotlib numpy
How to Run
In your terminal, navigate to the project folder and run:

✨ Example
Input:

makefile
Copy
Edit
List: 1, 3, 5, 7, 9, 11, 13, 15
Target: 7
Output:
The algorithm will show how it narrows down and finds 7 step-by-step.

👩‍💻 Author
Made with ❤️ by [ARJUMAND AFREEN TABINDA]

📜 License
This project is open-source and free to use under the MIT License.