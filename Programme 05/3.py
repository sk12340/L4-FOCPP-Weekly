import sys
args = sys.argv[1:]
if not args:
    print("No arguments provided.")
else:
    shortest = min(args, key=len)
    print(f"Shortest argument: {shortest}")