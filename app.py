import os
import tornado.ioloop
import config
import router


def main():
    app = tornado.web.Application(
        router.routes,
        debug=True,
        autoreload=True
    )
    app.listen(os.environ.get("PORT", config.port))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
