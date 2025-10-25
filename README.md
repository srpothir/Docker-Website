# Madhav Pothireddy - Personal Website

A modern, responsive personal portfolio website built with HTML, CSS, and JavaScript, containerized with Docker.

## 🚀 Quick Start with Docker

### Prerequisites
- Docker installed on your system
- Docker Compose (usually comes with Docker Desktop)

### Running the Website

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the website**
   Open your browser and navigate to: `http://localhost:8080`

### Alternative Docker Commands

**Build the image:**
```bash
docker build -t madhav-personal-website .
```

**Run the container:**
```bash
docker run -d -p 8080:80 --name madhav-website madhav-personal-website
```

**Stop the container:**
```bash
docker stop madhav-website
docker rm madhav-website
```

## 🧪 Testing

Run the test suites to verify everything is working:

```bash
# Test website functionality
python test_website_functionality.py

# Test Docker deployment
python test_docker_deployment.py
```

## 📁 Project Structure

```
├── Cursor/                 # Website files
│   ├── index.html         # Homepage
│   ├── about.html         # About page
│   ├── contact.html       # Contact page
│   ├── projects.html      # Projects page
│   ├── resume.html        # Resume page
│   ├── styles.css         # Main stylesheet
│   └── images/            # Image assets
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .dockerignore         # Docker ignore file
├── test_website_functionality.py  # Website tests
├── test_docker_deployment.py      # Docker tests
└── .github/workflows/    # GitHub Actions
```

## 🐳 Docker Configuration

The website is containerized using:
- **Base Image**: nginx:alpine (lightweight and efficient)
- **Port**: 8080 (host) → 80 (container)
- **Container Name**: madhav-personal-website
- **Restart Policy**: unless-stopped

## 🔧 Development

### Local Development (without Docker)
Simply open `Cursor/index.html` in your browser or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server Cursor -p 8000
```

### Making Changes
1. Edit files in the `Cursor/` directory
2. Rebuild the Docker image: `docker-compose up --build`
3. Test your changes at `http://localhost:8080`

## 🚀 Deployment

### GitHub Pages
The website is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the main branch.

### Manual Deployment
1. Build the Docker image
2. Push to your preferred container registry
3. Deploy to your hosting platform

## 📱 Features

- ✅ Responsive design (mobile-friendly)
- ✅ Modern, clean UI
- ✅ Contact form
- ✅ Project showcase
- ✅ Resume/CV section
- ✅ Docker containerization
- ✅ Automated testing
- ✅ CI/CD with GitHub Actions

## 🛠️ Technologies Used

- HTML5
- CSS3 (with Flexbox and Grid)
- JavaScript (ES6+)
- Docker
- Nginx
- GitHub Actions

## 📄 License

© 2024 Madhav Pothireddy. All rights reserved.

## 📞 Contact

- **Email**: [Your Email]
- **LinkedIn**: [Your LinkedIn]
- **GitHub**: [Your GitHub]

---

**Note**: This website is containerized and ready for deployment on any Docker-compatible platform.
