require_relative 'config'

class Cli
  def call_api
    api_client = Hubspot::Client.new(access_token: access_token)
    retries = 0
    max_retries = 3
    while retries < max_retries
      begin
        puts "Start requests: #{retries + 1}"
        api_client.crm.contacts.basic_api.get_page
        break  # Exit the loop if the API call succeeds
      rescue Hubspot::Crm::Contacts::ApiError => e
        if e.code == 429
          puts 'Rate limit exceeded, retrying in 5 seconds...'
          sleep(5)
          retries += 1
        else
          raise  # Reraise the exception if it's not a rate limit error
        end
      end
    end
  end
end


threads = []
200.times do
  threads << Thread.new do
    Cli.new.call_api
  end
end

threads.each(&:join)
