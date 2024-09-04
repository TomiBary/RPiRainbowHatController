import base64

def encode_b64(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

def decode_b64(data):
    return base64.b64decode(data.encode('utf-8')).decode('utf-8')

text = input("Text to encode: ")
encoded = encode_b64(text)
decoded = decode_b64(encoded)
print(text, encoded, decoded)

print(decode_b64(input("Decode: ")))



# #run manually
# pg_ctl -D /opt/homebrew/Cellar/postgresql@16 -o "-p 5441" start
# LC_ALL="C" /opt/homebrew/opt/postgresql@16/bin/postgres -D /opt/homebrew/var/postgresql@16

# export PGPORT=5441
# export PGDATA=/Users/tomas.bares/Library/PostgreSQL/16/data

# brew services restart postgresql@16

# pg_ctl -o "-p 5441" start
# pg_ctl status