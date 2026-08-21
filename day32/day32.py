"""
day32

Author:ignorant-fool
Version:0.1
Date:2026/8/21
"""

# project123 - 可插拔的哈希算法(策略模式)

# class StreamHasher:
#     """哈希摘要生成器"""
#
#     def __init__(self, alg='md5', size=4096):
#         self.size = size
#         alg = alg.lower()
#         self.hasher = getattr(__import__('hashlib'), alg)()
#
#     def __call__(self, stream):
#         return self.to_digest(stream)
#
#     def to_digest(self, stream):
#         """生成十六进制形式的摘要"""
#         for buf in iter(lambda: stream.read(self.size), b''):
#             self.hasher.update(buf)
#         return self.hasher.hexdigest()
#
# def main():
#     """主函数"""
#     hasher1 = StreamHasher()
#     with open('头像.jpg', 'rb') as stream:
#         print(hasher1.to_digest(stream))
#     hasher2 = StreamHasher(alg='sha1')
#     with open('头像.jpg', 'rb') as stream:
#         print(hasher2(stream))
#
# if __name__ == '__main__':
#     main()