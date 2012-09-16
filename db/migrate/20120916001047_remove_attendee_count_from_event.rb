class RemoveAttendeeCountFromEvent < ActiveRecord::Migration
  def change
    remove_column :events, :attendee_count
  end
end
