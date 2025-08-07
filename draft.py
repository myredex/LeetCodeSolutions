def generate_binary(n):
    def backtrack(s):
        if len(s) == n:
            print(s)
            return
        backtrack(s + "0")
        backtrack(s + "1")

    backtrack("")
generate_binary(2)