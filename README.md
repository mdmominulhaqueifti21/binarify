# Binarify

**Binarify** is a simple Python module that helps you convert English letters, words, or numbers into binary and convert them back into normal text.

It supports:
- Text to Binary
- Binary to Text

---

## 📦 Installation

Install this package directly using `pip`:

```bash
pip install binarify


Here is a basic example of how to use Binarify:

from binarify import Binarify

# Create an instance of the converter
b = Binarify()

# Convert text to binary
binary = b.to_binary("Hello")
print("Binary:", binary)

# Convert binary back to text
text = b.from_binary(binary)
print("Text:", text)

