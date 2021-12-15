import abc

class SocialMediaApp(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def like_posts(self):
        pass

    @abc.abstractmethod
    def publish_posts(self):
        pass


    @classmethod
    def __subclasshook__(cls, C):
        if cls is SocialMediaApp:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class Facebook:
    def like_posts(self):
        return "Yes you can like posts"

    def publish_posts(self):
        return "Yes you can publish posts"


print(issubclass(Facebook,SocialMediaApp)) #prints true since Facebook has all the abstract methods of SocialMediaApp