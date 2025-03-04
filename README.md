# Img2LateX
Img2LateX using Ollama, pure Go, HTML,CSS,JS and Python, rather than Gradio like others structure. You can use it in CLI or Web UI.

I want to crate a simple tool, no showy UI, no any useless animation, so it looks like not cool. So you can use it as a simple tool. Or learn a simple structure of AI application.

This is still in developing. So it may have some bugs or issues. If you find one or want new features, please tell me.

## Usage
You can delay it in other device.

First, you need install [Ollama](https://ollama.com/). It doesn't matter that you use in Docker container or in host, because I use cURL, rather than Python package `ollama`.
>Now I use [llama3.2-vision](https://ollama.com/library/llama3.2-vision) to implement this tool. I will finetune a model or find a better model to do it, you can know why in "Performance".

Then, download llama3.2-vision:

```
ollama pull llama3.2-vision
```

> It is unnecessary to run it before starting server. If model is installed , ollama service will auto load model when you request. (Ollama auto works as a service after boot)

You also need install packages `requests` and `pandas`:

```
pip install requests pandas
```

>I use `pandas` for json. Because `json` doesn't work nice for base64 of image. 

Then install Go, I use it to build server. You can see offical documents, it is a little complex.

And you can use below command to run service:

```
go run main.go
```

### In browser
Now you can use it in browser, link is http://localhost:8080, or `http://<IP-Address>:8080` when you run it in other device:



https://github.com/user-attachments/assets/a64b4611-b976-4b1f-be2d-2fe9fdf415ee



If you want to upload new image, please refresh page.

### Compile into a binary
You can use below command to build entire project to a binary (excluding Ollama):

```
go build -o bin/img2latex
```

Now you can using it like a program:

```
./bin/img2latex 
Server started at http://<IP-Address>:8080
```

### In terminal(CLI)
Run command below:

```
$ python ./ca.py uploads/up_file 
$$
r = \frac{\sum_{i=1}^{n}\left(x_i - x\right)\left(y_i - y\right)}{\sqrt{\left(\sum_{i=1}^{n}\left(x_i-x\right)^2\right) \left(\sum_{i=1}^{n}\left(y_i-y\right)^2\right)}}\\
$$
```

You can convert any image by path.

> Why I use `python ./img2latex.py`, rather `!#/usr/bin/python`. Because maybe your device has many version pythons, it is bad to work. 


## Todos
- add clear button. (Now it via refresh page)
- add menus to output more format subtitles/text.
- develop REST APIs.
- fix Performance Issues.
- add more informations in log, such as start time....
- maybe I can add button to stop running model, to fix issues.

## Performance and Issues
Now I use [llama3.2-vision](https://ollama.com/library/llama3.2-vision) to implement this tool. 

I will finetune a model to do it, because:
- This model has 2 min size is 11B (in 3060, it uses 11346MiB VRAM). This is not good for many user.
- 1 formula will take 1-5 seconds(in 3060), I think it can better. If ollama suspended, it will reload model and spend over 10 seconds. Too long for many formulas, but still faster than you type LateX codes by hand. 
> My friend have a M4 Pro (10 cores GPU) MacBook Pro, we test it. I remember it works little slower than 3060. Just for reference. 
>If you find my memory is wrong, please tell me! And if you test you device, please tell me, I will record it for people to reference.
- If you run the same image repeatly, it works so bad. If you meet this problem, please use `ollama stop` to stop running model, or `kill` to kill PID of `/usr/local/bin/ollama`(you can see it in `nvidia-smi`).

So, I need finetune a model. Due to I am a newer for ML/DL, I need time to learn that. 