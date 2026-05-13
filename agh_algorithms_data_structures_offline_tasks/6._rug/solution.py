class Solution:
    def solve(self):
        import sys

        def main():
            input_data = sys.stdin.read().split()

            if not input_data:
                return

            q = int(input_data[0])

            queries = [int(x) for x in input_data[1:q + 1]]

            if not queries:
                return

            max_q = max(queries)

            max_n = max_q - 1
            if max_n < 0:
                max_n = 0



        if __name__ == '__main__':
            main()
    