1. Follow the instruction from this page and clone a "Just-the-class" into your new repository.
2. Install dependency Jekyll
	1. "**Ruby+Devkit**"
		- Ruby: a programming language
		- RubyGem: a package manager of Ruby
		- Use `gem --version` to verify the installation
	2. Jekyll: A package / library written in Ruby language 
		- Use `gem install jekyll` to install jekyll
	3. Bundler:
		- Use `gem install bundler` to install it
3. Test github page locallly
	- https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll
	- Open cmd and navigate to the folder containing the page
	- Run `bundle install`: 
		- Bundler, which is a dependency management tool for Ruby projects, reads the Gemfile located in the project directory. The Gemfile lists all the gems (Ruby libraries) required by the project.
		- Bundler checks if the required gems are already installed on your system. If they are, it ensures that the correct versions are installed. If the required gems are not present or the versions do not match, Bundler proceeds to install them.
	- Then, run `bundle exec jekyll serve` in the same file
1. Make the webpage online
	- Go to settings > pages > Build and deployment. `main` branch and `/(root)` folder. 
	- The webpage will be deployed and live in your own github domain. Such as:
		- https://pakkinlau.github.io/prog-for-humanists-web/
		- 