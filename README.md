# Test Publish

A minimal Python package for testing PyPI publishing with Poetry and GitHub Actions.

## Features

- 📦 Poetry for dependency management
- 🚀 GitHub Actions for CI/CD
- 🔄 Semantic versioning with semantic-release
- ✅ Automated PR checks with commitlint
- 📝 Conventional commit validation

## Installation

```bash
pip install test-publish
```

## Usage

```python
from test_publish import hello

# Simple greeting
print(hello())  # Output: Hello, World!

# Custom greeting
print(hello("Python"))  # Output: Hello, Python!
```

## Development

### Setup

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install Node.js (for semantic-release):
```bash
# On macOS with Homebrew
brew install node

# On Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

3. Install Python dependencies:
```bash
poetry install
```

4. Install Node.js dependencies:
```bash
npm install
```

5. Activate the virtual environment:
```bash
poetry shell
```

### Running Tests

```bash
poetry run pytest
```

### Code Quality

Run linting and formatting:

```bash
poetry run black src tests
poetry run ruff check src tests
```

## Releasing

This project uses **semantic-release** (Node.js) for automated versioning and publishing.

### Commit Message Format

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: A new feature (triggers minor version bump, e.g., 1.0.0 → 1.1.0)
- `fix`: A bug fix (triggers patch version bump, e.g., 1.0.0 → 1.0.1)
- `perf`: Performance improvement (triggers patch version bump)
- `docs`: Documentation only changes (no version bump)
- `style`: Changes that don't affect code meaning (no version bump)
- `refactor`: Code change that neither fixes a bug nor adds a feature (no version bump)
- `test`: Adding missing tests (no version bump)
- `build`: Changes to build system or dependencies (no version bump)
- `ci`: Changes to CI configuration (no version bump)
- `chore`: Other changes that don't modify src or test files (no version bump)
- `revert`: Reverts a previous commit (no version bump)

**Breaking Changes:**

To indicate a breaking change (triggers major version bump, e.g., 1.0.0 → 2.0.0), add `!` after the type:

```
feat!: breaking API change
feat(api)!: breaking change in API
fix!: breaking fix

OR use BREAKING CHANGE in footer:

feat: add new feature

BREAKING CHANGE: this changes the API
```

**Examples:**
```
feat: add new greeting function
fix: resolve encoding issue in hello function
feat(api): add support for custom greetings
fix(auth)!: change authentication flow (breaking)
docs: update installation instructions
perf: improve hello function performance
```

### Creating a Release

1. Ensure all commits since the last release follow the conventional commit format
2. Go to **Actions** → **Semantic Release**
3. Click **"Run workflow"**
4. Select branch (usually `main`)
5. Click **"Run workflow"**

The workflow will automatically:
- ✅ Analyze commits to determine the version bump (major/minor/patch)
- ✅ Update version in `pyproject.toml` and `src/test_publish/__init__.py`
- ✅ Generate/update `CHANGELOG.md`
- ✅ Create a git commit and tag (e.g., `v1.2.3`)
- ✅ Build the package using Poetry
- ✅ Publish to PyPI
- ✅ Create a GitHub release with release notes

### Pull Request Checks

When you open a PR, the CI will automatically:
- ✅ Validate that the **PR title** follows the conventional commit format
- ✅ Run linters (Black and Ruff)
- ✅ Execute tests with coverage

**Note:** Individual commit messages in the PR are NOT validated. This is intentional for a **squash merge workflow**, where:
- Feature branch commits can have any format (WIP commits, fixup commits, etc.)
- Only the PR title matters - it becomes the commit message when squashed
- semantic-release reads the squashed commit (PR title) from main branch

**PR Title Examples:**
```
✅ feat: add user authentication
✅ fix: resolve memory leak in parser
✅ feat(api)!: breaking change to REST API
❌ Added some new features (not conventional format)
❌ WIP: work in progress (not a valid type)
```

### Recommended GitHub Settings

For squash merge workflow, configure your repository:
1. Go to **Settings** → **General** → **Pull Requests**
2. Allow only **"Squash and merge"**
3. Disable "Allow merge commits" and "Allow rebase merging"
4. This ensures the PR title always becomes the commit message

## Configuration

### PyPI Token

To publish to PyPI, add your PyPI token as a GitHub secret:

1. Generate a PyPI token at https://pypi.org/manage/account/token/
2. Add it as `PYPI_TOKEN` in your repository secrets

### Customization

Edit `pyproject.toml` to customize:
- Package name
- Author information
- Repository URLs
- Python version constraints
- Dependencies

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with conventional commits
4. Push to your fork
5. Open a Pull Request

The PR checks will automatically validate your commit messages.
