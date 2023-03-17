import qrcode
img = qrcode.make('Github webhook')
img.save("github_webhook.png")
