# 🤝 Contributing to CredSleuth

Thank you for your interest in contributing to CredSleuth! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful, inclusive, and professional when contributing to this project.

## How to Contribute

### 1. Reporting Bugs 🐛

If you discover a bug, please create an issue with:

- **Title:** Clear, descriptive title
- **Description:** Detailed explanation of the bug
- **Steps to Reproduce:** Exact steps to reproduce the issue
- **Expected Behavior:** What should happen
- **Actual Behavior:** What actually happens
- **Environment:** Python version, OS, relevant dependencies
- **Screenshots/Logs:** Any relevant output or errors

### 2. Suggesting Enhancements ✨

For feature requests:

- **Title:** Clear feature description
- **Motivation:** Why this feature would be useful
- **Proposed Implementation:** Your thoughts on how it could work
- **Examples:** Use cases or examples

### 3. Code Contributions 💻

#### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/CredSleuth.git
cd CredSleuth

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install pytest black flake8 pytest-cov
```

#### Making Changes

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Follow the existing code style
   - Add comments for complex logic
   - Keep functions focused and modular

3. **Code Standards:**
   - Use Python 3.8+ features
   - Follow PEP 8 style guide
   - Write docstrings for all functions
   - Use type hints where appropriate

4. **Test your changes:**
   ```bash
   python -m pytest
   ```

5. **Format your code:**
   ```bash
   black .
   flake8 .
   ```

#### Commit Guidelines

- Use clear, descriptive commit messages
- Reference related issues: `Fixes #123`
- Keep commits atomic and logical

Good commit message examples:
```
Add support for detecting Slack API tokens
Fix issue with file encoding detection
Refactor pattern matching logic for better performance
```

#### Pull Request Process

1. **Update documentation** if you're adding features
2. **Add tests** for new functionality
3. **Update CHANGELOG.md** with your changes
4. **Create a pull request** with:
   - Clear title and description
   - Reference to related issues
   - Explanation of changes
   - Test results
   - Screenshots (if applicable)

### Areas for Contribution

#### 🔐 Credential Patterns
- Add detection for new credential types
- Improve existing pattern accuracy
- Reduce false positives
- Optimize pattern matching performance

#### 🌍 Internationalization
- Add support for other languages
- Translate documentation
- Localize error messages

#### 📊 Reporting
- Enhance HTML report design
- Add new report formats (PDF, CSV, etc.)
- Improve data visualization
- Add customizable report templates

#### ⚡ Performance
- Optimize scanning algorithms
- Reduce memory usage
- Parallelize scanning operations
- Add progress indicators

#### 🧪 Testing
- Increase test coverage
- Add integration tests
- Create test fixtures
- Improve test documentation

#### 📚 Documentation
- Improve existing docs
- Add tutorials and guides
- Create video guides
- Add more examples

## Development Tips

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=scanner

# Run specific test file
pytest test_files/test_detector.py
```

### Project Structure
```
CredSleuth/
├── scanner/
│   ├── detector.py      # Main detection logic
│   ├── git_scanner.py   # Git history scanning
│   └── reporter.py      # Report generation
├── templates/
│   └── report.html      # HTML report template
├── test_files/          # Test data and test cases
├── main.py              # Entry point
└── requirements.txt     # Dependencies
```

### Key Files to Know

- **scanner/detector.py** - Core regex patterns and detection logic
- **scanner/reporter.py** - JSON and HTML report generation
- **main.py** - CLI interface and flow control

## Code Style Guide

### Python Style
```python
# Good: Clear, well-documented functions
def scan_file(file_path: str) -> List[Dict]:
    """
    Scan a file for credential patterns.
    
    Args:
        file_path: Path to the file to scan
        
    Returns:
        List of findings with details
    """
    # Implementation
    pass

# Bad: Unclear naming and no documentation
def scan(f):
    # scan file
    pass
```

### Naming Conventions
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`

## Questions?

- Check existing issues and discussions
- Review documentation
- Open a discussion thread
- Reach out to maintainers

## Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Credited in release notes
- Recognized for significant contributions

## Additional Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Documentation](https://git-scm.com/doc)
- [Regex Testing Tool](https://regex101.com/)
- [GitHub Guides](https://guides.github.com/)

---

Thank you for contributing to CredSleuth! 🙏
