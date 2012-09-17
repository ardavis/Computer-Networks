json.(@attendees.each) do |json, attendee|
  json.(attendee, :id, :event_id, :name)
end