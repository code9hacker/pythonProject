# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.
    import hashlib
    msg = bytes("test:ing", 'utf-8')
    answer = hashlib.sha1("LongSecretKeyYouWontBeAbleToBruteForce3".encode('raw_unicode_escape') + msg).hexdigest()
    print(answer)
    signature = "84cd4f0b442410e719d10545bccef5b470252c48"
    if answer == signature:
        print("yay")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
