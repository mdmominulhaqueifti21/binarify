class Binarify:
    def __init__(self, spacing=True):
        self.spacing = spacing

    def to_binary(self, text):
        binary_output = []
        for char in text:
            binary = format(ord(char), '08b')
            binary_output.append(binary)
        return ' '.join(binary_output) if self.spacing else ''.join(binary_output)

    def from_binary(self, binary_string):
        if ' ' in binary_string:
            binaries = binary_string.split()
        else:
            binaries = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        return ''.join([chr(int(b, 2)) for b in binaries])
