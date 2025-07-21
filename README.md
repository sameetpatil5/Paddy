# 🐶 PaddyPDF – The Ultimate PDF Tools API

![Build](https://github.com/your-username/paddy/actions/workflows/ci.yml/badge.svg)
[![Deploy to Render](https://img.shields.io/badge/Render-Deployed-success?logo=render)](https://paddy-backend-b2z6.onrender.com)
[![Docker](https://img.shields.io/badge/Docker-Available-blue?logo=docker)](yet-to-be-pushed)

**Paddy** is a lightweight, Dockerized **FastAPI** project that provides blazing-fast PDF tools via REST APIs.  
Whether you're merging files, converting images/Markdown to PDF, or extracting images – **Paddy has you covered**.

> 🔧 Plug. 🔄 Process. 📦 Done.

---

## 🌐 Live Demo

🔗 [paddy-backend-b2z6.onrender.com](https://paddy-backend-b2z6.onrender.com)  
📜 [Swagger Docs](https://paddy-backend-b2z6.onrender.com/docs)

---

## 🚀 Features

- ✅ Merge multiple PDFs into one
- 🖼️ Convert images (or image sets) to a single PDF
- 📝 Convert Markdown to print-ready PDF
- 🧵 Convert PDF to image
- 📦 Fully Dockerized
- ⚙️ CI/CD with GitHub Actions
- 📈 Prometheus metrics for observability

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- Docker 🐳
- GitHub Actions CI/CD ⚙️
- Prometheus + Grafana

---

## 🛠️ API Endpoints

| Method | Endpoint           | Description                        |
| ------ | ------------------ | ---------------------------------- |
| GET    | `/`                | Welcome message                    |
| POST   | `/merge`           | Merge PDF files                    |
| POST   | `/images-to-pdf`   | Convert one or more images to PDF  |
| POST   | `/markdown-to-pdf` | Convert Markdown file to PDF       |
| POST   | `/extract-images`  | Extract embedded images from a PDF |
| GET    | `/metrics`         | Prometheus metrics                 |
| GET    | `/docs`            | Swagger UI for API testing         |

---

## 🧪 Running Locally

```bash
git clone https://github.com/your-username/paddy.git
cd paddy
pip install -r requirements.txt
uvicorn app.main:app --reload
````

Or using Docker:

```bash
docker build -t paddy .
docker run -p 8000:80 paddy
```

---

## 🚀 Deployment

Paddy is **cloud-ready**:

- Easily deploy on **Render**, **Fly.io**, or even **EC2**
- Include a `render.yaml` for 1-click deploys

---

## 📊 Monitoring

Prometheus metrics are exposed at `/metrics` when enabled.
Set up with Grafana dashboards for insights into PDF activity and app health.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

Want to add more PDF tools like:

- Text extraction
- Page reordering
- Digital signature support?

Let's build Paddy into the most powerful open-source PDF API together 🛠️

---

## 🧾 License

MIT © 2025 Sameet Patil

---

Built with ❤️ by [Sameet Patil](https://github.com/sameetpatil5)
