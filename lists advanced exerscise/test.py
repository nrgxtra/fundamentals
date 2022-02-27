class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


print(Comment('Gosho', 'says hi to Pesho', 3).__dict__)
print(Comment('Gosho', 'says hi to Pesho').__dict__)
