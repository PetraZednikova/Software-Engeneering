class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        self._latest_news = news
        self.notify_subscribers()

    def get_news(self):
        return self._latest_news


class Subscriber:
    def __init__(self, name, publisher):
        self._name = name
        self._publisher = publisher
        self._publisher.subscribe(self)

    def update(self):
        print(f'{self._name} dostal správu: {self._publisher.get_news()}')


# Príklad použitia
if __name__ == "__main__":
    publisher = NewsPublisher()

    subscriber1 = Subscriber("Odberateľ 1", publisher)
    subscriber2 = Subscriber("Odberateľ 2", publisher)

    publisher.add_news("Novinka: Observer Pattern v Pythone!")

    # Odhlásenie odberateľa
    publisher.unsubscribe(subscriber1)

    publisher.add_news("Ďalšia novinka: Observer Pattern je stále skvelý!")