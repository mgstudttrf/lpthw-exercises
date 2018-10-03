from sys import argv

prompt = ">"

script, username = argv

print(f"hi {username}. script {script} is talking")
print("do u like me")
like = input(prompt)
print(" are u tired of dese printin")
tired = input(prompt)
print(f"""
        aihht. so you said {like} about liking me
        and you said that '{tired}' about tiredness from printing
        """)
