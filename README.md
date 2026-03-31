# README

This procedure describes how to embed code into the book versions of units.

1. Upload a script file to the code-snippets repository - <https://github.com/c4r-io/code-snippets> 

2. When viewing the file on github in a web browser, click the Raw button:
![screenshot of github with `raw` button](raw-button.png)

3. Copy the URL in the web browser. This is a direct link to the code file.

We can now move to shorthand!

4. In Shorthand, go to the "story" with the relevant lesson.

5. Navigate to the appropriate location in the lesson, and where the code snippet should go, make sure that it is a section boundary. (This may require splitting an existing text section into separate sections.)

6. Click on the `+` button to add a new section. Under the Default options, scroll down to the bottom to `Custom HTML`

7. In the resulting HTML box, copy-paste the following block.

8. Make sure to set the programming language and the code file as appropriate in the middle of the code block.

```
<!-- Highlight.js CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/atom-one-light.min.css">
 
<!-- Highlight.js JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js"></script>

<style>
  code.hljs {
    counter-reset: line;
  }

  code.hljs .line::before {
    counter-increment: line;
    content: counter(line);
    display: inline-block;
    width: 2em;
    margin-right: 1em;
    text-align: right;
    color: #a0a1a7;
    border-right: 1px solid #d0d0d0;
    padding-right: 0.5em;
    user-select: none;
    -webkit-user-select: none;
  }
</style>

<!-- FIX THE LANGUAGE BELOW IF NEEDED -->
<pre><code id="raw-code" class="language-python"></code></pre>

<!-- REPLACE THE URL WITH THE CODEFILE LINK -->
<script>
  const rawUrl = 'https://raw.githubusercontent.com/c4r-io/code-snippets/refs/heads/main/test.py';

  fetch(rawUrl)
    .then(response => {
      if (!response.ok) throw new Error('File not found');
      return response.text();
    })
    .then(content => {
      const block = document.getElementById('raw-code');
      block.textContent = content;
      hljs.highlightElement(block);
      // Wrap each line in a span after highlighting
      block.innerHTML = block.innerHTML
        .split('\n')
        .map(line => `<span class="line">${line}</span>`)
        .join('\n');
    })
    .catch(error => console.error('Error:', error));
</script>
```
