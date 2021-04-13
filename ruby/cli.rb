require_relative 'config'

class Cli
  def run
    1000.times do
      Thread.new { call_api }
    end
  end

  private

  def call_api
    api = Hubspot::Crm::Objects::BasicApi.new
    api.get_page('contact', auth_names: 'hapikey')
  rescue Hubspot::Crm::Objects::ApiError => e
    p e
  end
end

Cli.new.run
