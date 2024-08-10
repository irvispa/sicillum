import binascii

hex_string = 'b3e2cdfdcdaccbd5e8f4cae4e6f5c9fff2aef1e2cccccccc'

# Convert hexadecimal string to bytes
hex_bytes = bytes.fromhex(hex_string)

# Decode bytes to text (assuming it's text encoded)
text = hex_bytes.decode('utf-8')

print(text)
