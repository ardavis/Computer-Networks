class AddDateToEvents < ActiveRecord::Migration
  def change
    add_column :events, :date, :date
    add_column :events, :start_time, :time
    add_column :events, :end_time, :time
  end
end
