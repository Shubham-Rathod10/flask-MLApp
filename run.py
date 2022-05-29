from app import create_app
env = 'dev'
app = create_app('config.' + env)
if __name__ == '__main__':
    app.run(port=app.config['PORT'],
            debug=True)
