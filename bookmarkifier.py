import sys

# TODO: scripting bookmark creation on browser?

if len(sys.argv) < 3:
    print('Usage: %s [src: JS file] [dst: bookmark URL file]' % (sys.argv[0]))
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

def wrap_in_block(js):
    return "(function () {" + js + "})()"

with open(src, "r") as f:
    raw_js_script = f.read().strip()
    one_liner_js = raw_js_script.replace("\r\n", " ").replace("\n", " ")

    js_url = "javascript:" + wrap_in_block(wrap_in_block(one_liner_js))

    print(js_url)
