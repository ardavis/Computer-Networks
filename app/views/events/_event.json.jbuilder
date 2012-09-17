json.(event, :id, :name, :desc, :date, :start_time, :end_time)
json.location [event.address, event.city, event.state].join(', ')
json.attendee_count event.attendance
json.attendees event.attendees, :id, :name
