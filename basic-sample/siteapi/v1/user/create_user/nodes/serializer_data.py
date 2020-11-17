from arkfbp.node import SerializerNode, CharFieldNode


# Editor your node here.


class SerializerData(SerializerNode):
    username = CharFieldNode(min_length=10, max_length=50)
    password = CharFieldNode(min_length=10, max_length=50)
    # nickname = CharFieldNode()
    # mobile = CharFieldNode()
    # email = CharFieldNode()

    class Meta:

        # 返回的字段
        fields = (
            'username',
            'password',
            'nickname',
            'mobile',
            'email',
        )

    def run(self, *args, **kwargs):
        print(f'Hello, SerializerData!')
        return super(SerializerData, self).run(*args, **kwargs)
