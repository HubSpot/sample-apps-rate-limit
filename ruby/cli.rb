require_relative 'config'

class Cli
  def run
    Thread.abort_on_exception = true
    Thread.report_on_exception = true
    1000.times do
      Thread.new { call_api }
      p :*
    end
  end

  private

  def call_api
    client = Hubspot::Client.new(access_token: access_token)
    api = client.crm.contacts.basic_api.get_page
  end
end

Cli.new.run
