viewTemplates.xlfSurveyDetailView = (model) ->
    """
    <label title="#{model.get("description") || ''}">
      <input type="checkbox">
      #{model.get("label")}
    </label>
    """
