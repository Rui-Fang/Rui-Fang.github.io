FROM ruby:3.2.2
WORKDIR /usr/src/app
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v 2.3.5 --no-document && bundle _2.3.5_ install
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--watch"]
