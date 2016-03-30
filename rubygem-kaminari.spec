#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-kaminari
Version  : 0.16.1
Release  : 6
URL      : https://rubygems.org/gems/kaminari-0.16.1.gem
Source0  : https://rubygems.org/gems/kaminari-0.16.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-actionpack
BuildRequires : rubygem-activesupport
BuildRequires : rubygem-capybara
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rr
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-tzinfo

%description
= Kaminari {<img src="https://travis-ci.org/amatsuda/kaminari.svg"/>}[http://travis-ci.org/amatsuda/kaminari] {<img src="https://img.shields.io/codeclimate/github/amatsuda/kaminari.svg" />}[https://codeclimate.com/github/amatsuda/kaminari] {<img src="http://inch-ci.org/github/amatsuda/kaminari.svg" alt="Inline docs" />}[http://inch-ci.org/github/amatsuda/kaminari]

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n kaminari-0.16.1
gem spec %{SOURCE0} -l --ruby > rubygem-kaminari.gemspec

%build
gem build rubygem-kaminari.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
kaminari-0.16.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/kaminari-0.16.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/.document
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/CHANGELOG.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_first_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_first_page.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_first_page.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_gap.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_gap.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_gap.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_last_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_last_page.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_last_page.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_next_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_next_page.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_next_page.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_page.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_page.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_paginator.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_paginator.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_paginator.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_prev_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_prev_page.html.haml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/app/views/kaminari/_prev_page.html.slim
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/config/locales/kaminari.yml
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_30.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_31.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_32.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_40.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_41.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/active_record_edge.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/data_mapper_12.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/mongo_mapper.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/mongoid_24.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/mongoid_30.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/mongoid_31.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/mongoid_40.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/sinatra_13.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/gemfiles/sinatra_14.gemfile
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/kaminari.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/generators/kaminari/config_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/generators/kaminari/templates/kaminari_config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/generators/kaminari/views_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/grape.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/helpers/action_view_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/helpers/paginator.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/helpers/sinatra_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/helpers/tags.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/hooks.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/active_record_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/active_record_model_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/active_record_relation_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/array_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/configuration_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/data_mapper_collection_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/data_mapper_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/mongo_mapper_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/mongoid_criteria_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/mongoid_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/page_scope_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/models/plucky_criteria_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/sinatra.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/lib/kaminari/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/config/config_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/active_record/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/active_record/models.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/data_mapper/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/data_mapper/models.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/mongo_mapper/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/mongo_mapper/models.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/mongoid/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/mongoid/models.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/rails_app.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/sinatra_app.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/views/alternative/kaminari/_first_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/views/alternative/kaminari/_paginator.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/views/kaminari/bootstrap/_page.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_app/views/kaminari/bootstrap/_paginator.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/fake_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/generators/views_generator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/helpers/action_view_extension_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/helpers/helpers_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/helpers/sinatra_helpers_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/helpers/tags_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/active_record/active_record_relation_methods_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/active_record/scopes_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/array_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/configuration_methods_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/data_mapper/data_mapper_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/mongo_mapper/mongo_mapper_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/models/mongoid/mongoid_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/requests/users_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/spec_helper_for_sinatra.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/support/database_cleaner.rb
/usr/lib64/ruby/gems/2.3.0/gems/kaminari-0.16.1/spec/support/matchers.rb
/usr/lib64/ruby/gems/2.3.0/specifications/kaminari-0.16.1.gemspec
