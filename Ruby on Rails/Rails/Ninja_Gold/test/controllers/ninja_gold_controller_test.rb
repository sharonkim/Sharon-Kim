require 'test_helper'

class NinjaGoldControllerTest < ActionDispatch::IntegrationTest
  test "should get initialize" do
    get ninja_gold_initialize_url
    assert_response :success
  end

  test "should get index" do
    get ninja_gold_index_url
    assert_response :success
  end

end
