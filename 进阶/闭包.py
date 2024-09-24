""''''
def otuer(logo):
    def inner(msg):
        print(f"<{logo}><{msg}><{logo}>")

    return inner

fn1=otuer("刘淼")("6666")
'''''
def outer(n1):
    def inner(n2):
        nonlocal n1
        n1+=n2
        print(n1)
    return inner

fn=outer(10)
fn(20)
fn(20)