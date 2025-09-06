# -*- coding: utf-8 -*-

from transformers import AutoConfig, AutoModel, AutoModelForCausalLM

from fla.models.routmem.configuration_routmem import RoutMemConfig
from fla.models.routmem.modeling_routmem import RoutMemForCausalLM, RoutMemModel

AutoConfig.register(RoutMemConfig.model_type, RoutMemConfig, exist_ok=True)
AutoModel.register(RoutMemConfig, RoutMemModel, exist_ok=True)
AutoModelForCausalLM.register(RoutMemConfig, RoutMemForCausalLM, exist_ok=True)


__all__ = ['RoutMemConfig', 'RoutMemForCausalLM', 'RoutMemModel']
