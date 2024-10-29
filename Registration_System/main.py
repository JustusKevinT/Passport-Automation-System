from website import create_application

app = create_application()

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5001)
