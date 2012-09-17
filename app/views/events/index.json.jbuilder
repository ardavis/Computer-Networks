json.(@events.each) do |json, event|
  json.partial! event
end