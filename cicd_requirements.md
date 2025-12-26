# Enterprise CI/CD Compatibility Rating Requirements

Analyze this repository using repomix and rate it (0-10) for enterprise CI/CD compatibility as a component in a larger system.

## Evaluation Criteria (Total: 0-10 points)

### 1. Build System (0-2 points)
- Modern build tools present (npm/yarn/pnpm, gradle, maven, cargo, go mod, etc.)
- Reproducible builds configured
- Dependency management properly set up
- Build scripts documented

### 2. Testing (0-2 points)
- Unit tests present
- Test framework configured (Jest, pytest, JUnit, etc.)
- CI test automation ready
- Test coverage reporting

### 3. CI/CD Configuration (0-2 points)
- GitHub Actions / GitLab CI / Jenkins files present
- Automated workflows defined
- Deployment pipelines configured
- Multi-environment support

### 4. Documentation (0-1 point)
- README with clear setup instructions
- API documentation (if applicable)
- Architecture/design documentation
- Contributing guidelines

### 5. Code Quality (0-1 point)
- Linting configured (ESLint, pylint, etc.)
- Code formatting tools (Prettier, Black, etc.)
- Static analysis tools present
- Pre-commit hooks

### 6. Containerization (0-1 point)
- Dockerfile present and well-structured
- Docker Compose for local development
- Kubernetes manifests (if applicable)
- Container best practices followed

### 7. Security (0-1 point)
- Dependency scanning configured
- Secret management practices
- Security scanning in CI
- No hardcoded credentials

## Overall Rating Scale

- **9-10**: Production-ready, enterprise-grade
- **7-8**: Well-structured, minor improvements needed
- **5-6**: Functional but needs significant CI/CD work
- **3-4**: Basic structure, major improvements required
- **0-2**: Minimal/no CI/CD infrastructure

## Output Format

```json
{
  "repo": "repo-name",
  "overall_rating": 8.5,
  "build_system": 2,
  "testing": 1.5,
  "cicd_config": 2,
  "documentation": 1,
  "code_quality": 1,
  "containerization": 0.5,
  "security": 0.5,
  "notes": "Brief analysis highlighting strengths and areas for improvement",
  "recommendation": "production-ready | needs-work | prototype"
}
```
