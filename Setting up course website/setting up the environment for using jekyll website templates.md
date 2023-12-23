1. Select a template you want 
	- From github: https://github.com/alshedivat/al-folio

#### Method 1: Use docker to setup the environment

#### Method 2: Install Jekyll and Ruby in the PC
1. Install dependency Jekyll
	1. "**Ruby+Devkit**"
		- Ruby: a programming language
		- RubyGem: a package manager of Ruby
		- Use `gem --version` to verify the installation
	2. Jekyll: A package / library written in Ruby language 
		- Use `gem install jekyll` to install jekyll
	3. Bundler:
		- Use `gem install bundler` to install it
2. Run jekyll and edit the website with local live server
	- https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll
	- Open cmd and navigate to the folder containing the page
	- Run `bundle install`: 
		- Bundler, which is a dependency management tool for Ruby projects, reads the Gemfile located in the project directory. The Gemfile lists all the gems (Ruby libraries) required by the project.
		- Bundler checks if the required gems are already installed on your system. If they are, it ensures that the correct versions are installed. If the required gems are not present or the versions do not match, Bundler proceeds to install them.
	- Then, run `bundle exec jekyll serve` in the same file
		- `bundle exec`: it ensure the following up command will be executed within the context of the project's dependencies. 
		- `jekyll serve`: `serve` is a Jekyll-specific command that builds your Jekyll site and starts a local development server. 
	- A local server address will be included in the output response. If it is not the case, in my trial, it is because `webbrick` is not bundled in Ruby3.0. To fix this, add `gem "webrick", ">= 1.7"` in the final line of `Gemfile` in the repo. 
3. Make the webpage online
	- Go to settings > pages > Build and deployment. `main` branch and `/(root)` folder. 
	- The webpage will be deployed and live in your own github domain. Such as:
		- https://pakkinlau.github.io/prog-for-humanists-web/
	- Notice that the update of github page takes time. You can see the progress in the github action 

![](../Pasted%20image%2020231217020056.png)
![](../Pasted%20image%2020231217020050.png)