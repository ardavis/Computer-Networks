class AttendeesController < ApplicationController

  before_filter :get_event

  def index
    #@attendees = Attendee.all
    @attendees = @event.attendees
  end

  def show
    @attendee = Attendee.find(params[:id])
  end

  def new
    @attendee = @event.attendees.new
  end

  def edit
    @attendee = Attendee.find(params[:id])
  end

  def create
    @attendee = @event.attendees.new(params[:attendee])
    logger.info "New Attendee #{@attendee.as_json}"

    respond_to do |format|
      if @attendee.save
        format.html {redirect_to @event, notice: 'Attendee was successfully added.' }
        format.json { render json: @attendee, status: :created, location: @attendee }
      else
        format.html {render :new}
        format.json { render json: @attendee.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    @attendee = Attendee.find(params[:id])

    if @attendee.update_attributes(params[:attendee])
      redirect_to @event, notice: 'Attendee was successfully updated.'
    else
      render :edit
    end
  end

  def destroy
    Attendee.find(params[:id]).destroy
    redirect_to @event
  end

  def get_event
    @event = Event.find(params[:event_id])
  end
end
