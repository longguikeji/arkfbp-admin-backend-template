from arkfbp.node import AuthTokenNode


# Editor your node here.
class VerifyPassword(AuthTokenNode):

    def get_ciphertext(self):
        return self.encrypt_password('123456')
