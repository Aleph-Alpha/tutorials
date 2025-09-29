export const copyToClipboard = async (text: string, html?: string) => {
  const htmlType = 'text/html'
  const textType = 'text/plain'

  const htmlBlob = new Blob([html || text], { type: htmlType })
  const textBlob = new Blob([text], { type: textType })
  if (!window.ClipboardItem) {
    await navigator.clipboard.writeText(text)
  } else {
    const data = [
      new window.ClipboardItem({
        [htmlType]: htmlBlob,
        [textType]: textBlob,
      }),
    ]

    await navigator.clipboard.write(data)
  }
}
