

# Hello! Should we talk?

<div style="display:flex; align-items:flex-start;">
  <div>
    This is my portfolio. I am:
    <ul>
      <li>👀 curious: human process & performance</li>
      <li>🌱 interested: python, rust</li>
      <li>💞️ collaborating: systems that work to create delightful experiences</li>
    </ul>
  </div>
  <img src="https://user-images.githubusercontent.com/76539355/214731371-78cb7bcb-996d-4108-9872-7af758ed5647.png" alt="A Maia" style="margin-left:1rem;">
</div>


# kjon &middot; django  
 
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/kjon-life/kjon_django) 
 ![GitHub License](https://img.shields.io/github/license/kjon-life/kjon_django)
 ![GitHub top language](https://img.shields.io/github/languages/top/kjon-life/kjon_django)
 ![W3C Validation](https://img.shields.io/w3c-validation/html?targetUrl=https%3A%2F%2Fkjon.life) 
 
This is a project that feeds my developer portfoio. To connect:  
- Mention me in an issue or pull request: @kjon-life  
- My friends connect on [Instagram: @kilo.jon](https://www.instagram.com/kilo.jon/)   
- [LinkedIn](https://www.linkedin.com/in/jonhwilliams) works as well.


### Project Overview:
* Gunicorn is a Python WSGI HTTP Server for UNIX, perfect for serving Django projects in production
* Postgres
* WhiteNoise to serve static files
* Authenticate with 2FA
* GitHub Actions deploys main to dev automatically

### Tech stack:
* Gunicorn
* Postgres
* django-environ - separate local,dev,prod
* Docker - to package Django apps as image
* flyctl - to build images, config toml, and deploy
* GitHub Actions - for CI/CD
* Fly.io - for the serverless hosting platform

```flyctl``` is a CLI tool from [Fly.io](http://fly.io)
You can read about it [here](https://fly.io/docs/hands-on/).

### History:  
#### Serverless hosted Django w Postgres
> 2024-04-07 2231  HRS 
* App deployed on fly.io and available at [https://kjon-django.fly.dev/](https://kjon-django.fly.dev/) or [https://django.jonhwilliams.com/](https://django.jonhwilliams.com/)  
* GitHub [repository](https://github.com/kjon-life/kjon_django) is now public. 
```bash
fly secrets set CSRF_TRUSTED_ORIGINS='https://kjon-django.fly.dev'
fly secrets set ALLOWED_HOSTS='kjon-django.fly.dev'
```

#### Local Django
* Postgres
* Using a templatemo-scholar template
![](hello/static/images/iterations/2024-04-06-23-28-17.png)

### Acknowledgements:

This project [depends](https://github.com/kjon-life/kjon-life/network/dependencies) on the copious contributions of others and is possible because of the following services:

- [Porkbun](https://porkbun.com/) - Domain registration and DNS management
- [Fly.io](https://fly.io/) - Application hosting platform
